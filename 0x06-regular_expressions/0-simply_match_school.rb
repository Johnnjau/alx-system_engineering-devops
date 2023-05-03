#!/usr/bin/env ruby

input_string = ARGV[0]
regex_pattern = /School/
matches = input_string.scan(regex_pattern)

puts "The input string '#{input_string}' contains the following matches for the regular expression '#{regex_pattern}':"
puts matches.join(", ")