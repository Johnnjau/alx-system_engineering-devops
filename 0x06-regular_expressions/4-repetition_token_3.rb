#!/usr/bin/env ruby

input_str = ARGV[0]

if input_str.match(/hbt*n/)
  puts input_str.scan(/hbt*n/).join
end