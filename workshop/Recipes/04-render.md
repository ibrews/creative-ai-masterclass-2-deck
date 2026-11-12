# Rendering

Use Movie Render Queue with map 04_Cinematic and sequence LS_LanternFestival, PNG frames, 1280×720, 24 fps, sequence range 0–287. Set a new output folder. Inspect actual frames from each camera cut.

For FFmpeg, inspect the actual filenames first. Example only, replace the pattern and start number with your real files:

```sh
ffmpeg -framerate 24 -start_number 0 -i "YOUR_ACTUAL_PATTERN.%04d.png" -c:v libx264 -pix_fmt yuv420p -crf 18 "new-review.mp4"
```

Keep the source frames. Decode the MP4 and inspect it visually. A command exit code does not certify the image.
