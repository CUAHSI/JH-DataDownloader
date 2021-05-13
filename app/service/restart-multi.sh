
for port in {8000..8007}; do
  sudo systemctl restart jh-downloader-multi@"${port}".service
done

