PANGOCAIRO_BACKEND=fc \
tesseract/src/training/ 
tesstrain.sh --fonts_dir fonts_n \
            --fontlist "Indie Flower"\
            --lang eng \
            --linedata_only \
            --langdata_dir langdata_lstm \
            --tessdata_dir tesseract/tessdata \
            --save_box_tiff \
            --maxpages 1 \
            --output_dir train \