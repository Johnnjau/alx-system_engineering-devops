#!/usr/bin/env ruby

input_str = ARGV[0]

if input_str.match(/hb?t?n/)
  puts input_str.scan(/hb?t?n/).join
end