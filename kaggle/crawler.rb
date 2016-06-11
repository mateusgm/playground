require 'nokogiri'
require 'open-uri'
require 'csv'
require 'openssl'

PARAMS = { :ssl_verify_mode => OpenSSL::SSL::VERIFY_NONE, 'User-Agent' => 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36' }
URL = 'https://www.kaggle.com/competitions/search?Query=&RewardColumnSort=Descending&SearchVisibility=AllCompetitions&ShowCompleted=true&ShowProspect=true&ShowOpenToAll=true&ShowPrivate=true&ShowLimited=true'
KADDLE = 'https://www.kaggle.com'

def number(str)
  n = str.to_s[/[\d\.,]+/]
  n.gsub(',', '').to_i unless n.nil?
end

CSV.open('competitions.csv', 'wb') do |csv|
  csv << [ 'name', 'link', 'prize', 'contestants', 'forum', 'scripts', 'votes', 'best_voted' ]
end

html = Nokogiri::HTML( open(URL) )

competitions = html.css('#competitions-table tr.finished-comp').map do |x|
  url = x.css('.competition-details a').first['href']
  url = "//www.kaggle.com" + url if url[0..1] == '/c'
  url = "https:" + url           if url['//']
  {
    name: x.css('.competition-details a').first.text,
    prize: number(x.css('td')[1].text),
    contestants: number(x.css('td')[2].text),
    link: url
  }
end



competitions.each do |x|
  print x[:name], "\n"
  doc  = open(x[:link], PARAMS).read
  html = Nokogiri::HTML( doc )
  x[:forum] = number(html.css('#compside-discussions h1').first.text) rescue ''
 
  id   = doc.scan(/competitionId = (\d+)/).flatten.first
  doc = open( "#{KADDLE}/c/#{id}/scripts/hot/widget", PARAMS ) rescue false 
  if doc
    html = Nokogiri::HTML( doc )
    x[:scripts] = number html.css('#compside-scripts h1').first.text
    x[:best_voted] = html.css('#compside-scripts .script-meta').map { |x| x.text.scan(/(\d+) Votes/).first }.flatten.map(&:to_i)
    x[:votes] = x[:best_voted].reduce(0, :+)
  end
 
  doc = open(x[:link] + '/forums', PARAMS ) rescue false 
  if doc
    html = Nokogiri::HTML( doc )
    link = html.css('.topiclist .forum-pages a').map { |x| "#{KADDLE}/#{x['href']}" }
    x[:best_replied] =
  end

  CSV.open('competitions.csv', 'ab') do |csv| 
    csv << [ x[:name], x[:link], x[:prize], x[:contestants], x[:forum], x[:scripts], x[:votes], x[:best_voted].to_s ]
  end
end
