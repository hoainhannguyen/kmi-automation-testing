module FileUtils
    def FileUtils.get_file_path(path)
        filePath = File.expand_path(path, __dir__)
        filePath
    end
end
