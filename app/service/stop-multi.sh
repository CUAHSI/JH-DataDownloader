
for port in {8000..8007}; do
  sudo systemctl stop jh-downloader-multi@"${port}".service
done

