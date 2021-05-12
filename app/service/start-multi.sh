
for port in {8000..8007}; do
  sudo systemctl enable jh-downloader-multi@"${port}".service
  sudo systemctl start jh-downloader-multi@"${port}".service
done

