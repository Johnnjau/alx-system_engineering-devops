#!/usr/bin/env ruby

input_str = ARGV[0]

if input_str.match(/School/)
  puts input_str.scan(/School/).join
end
