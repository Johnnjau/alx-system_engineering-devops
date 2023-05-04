#!/usr/bin/env ruby

regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

match_data = ARGV[0].scan(regex)

output = match_data.map do |match|
  "#{match[1]},#{match[2]},#{match[3]}"
end.join("\n")

puts output