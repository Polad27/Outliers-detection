def data_targz_download(url, directory, filename):
  
  import os
  import tarfile
  import urllib.request
  
  url = url
  file_tmp = urllib.request.urlretrieve(url, filename=None)[0]
  base_name = os.path.basename(url)
  file_name, file_extension = os.path.splitext(base_name)
  tar = tarfile.open(file_tmp)
  f = tar.extractfile(directory + filename).read().decode('utf-8')
  f = str(f)
  
  return f