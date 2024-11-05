module Jekyll
  module Money
    def monetary(value, separator=",")
      readable = sprintf("%.2f", value).split('.')
      readable[0] = readable[0].gsub(/(\d)(?=(\d\d\d)+(?!\d))/, "\\1#{separator}")
      return "#{readable.join('.')}"
    end
    def categoryName(value, separator=":")
      # If the value doesn't contain the separator, return it as is
      return value + " (total)" unless value.include? separator
      # If the value is the hard-coded value "Income:Donations", return "Donations"
      return "Donations" if value == "Income:Donations"
      # split the value on the separator, only return the last part,
      # but prefix it with as many spaces as there are separators
      return '<span class="indent"></span>' * value.count(separator) + "↦ " + value.split(separator).last
    end
  end
end

Liquid::Template.register_filter(Jekyll::Money)
