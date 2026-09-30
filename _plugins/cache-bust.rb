# based on https://distresssignal.org/busting-css-cache-with-jekyll-md5-hash
# https://gist.github.com/BryanSchuetz/2ee8c115096d7dd98f294362f6a667db
require 'digest/md5'

module Jekyll
  module CacheBust
    def bust_file_cache(file_name)
      local_file_name = file_name.slice(file_name.index('assets/')..-1)
      digest = Digest::MD5.hexdigest(File.read(local_file_name))
      [file_name, '?', digest].join
    end
  end
end

Liquid::Template.register_filter(Jekyll::CacheBust)
