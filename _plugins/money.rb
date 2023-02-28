module Jekyll
  module Money
    def monetary(value, separator=",")
      readable = sprintf("%.2f", value).split('.')
      readable[0] = readable[0].gsub(/(\d)(?=(\d\d\d)+(?!\d))/, "\\1#{separator}")
      return "#{readable.join('.')}"
    end
  end
end

Liquid::Template.register_filter(Jekyll::Money)
