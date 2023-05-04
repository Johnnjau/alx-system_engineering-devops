#!/usr/bin/env ruby

input_str = ARGV[0]

if input_str.match(/hbt{2,5}n/)
    puts input_str.scan(/hbt{2,5}n/).join
end