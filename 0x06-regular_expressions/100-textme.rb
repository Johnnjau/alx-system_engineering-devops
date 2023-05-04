#!/usr/bin/env ruby

if ARGV.empty?
  puts "Please provide a string argument."
  exit
end

regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

match_data = ARGV[0].scan(regex)

if match_data.empty?
  puts "No matches found."
  exit
end

output = match_data.map do |match|
  "#{match[1]},#{match[2]},#{match[0]}"
end.join("\n")

puts output
