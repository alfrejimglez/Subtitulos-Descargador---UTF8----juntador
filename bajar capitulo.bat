cd C:\Users\alfre\OneDrive\Documentos\Lahorafosca
ffmpeg -i "https://manifest.prod.boltdns.net/manifest/v1/hls/v4/aes128/6057955885001/df9bf581-bcef-4531-a8db-80563d7745dc/10s/master.m3u8?fastly_token=NjcxYWYzZGVfMDZhMTQxNTM2ODc0ODYxYjlhOWVjZDgwMWVhM2QwZGJkYTY1ZDY5NmYwMGI1ZWY2ZDlhY2FlNGE2ZGQ0N2IyNA%3D%3D" -c copy -bsf:a aac_adtstoasc output.mp4
