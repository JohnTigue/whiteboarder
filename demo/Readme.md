# Whiteboarder demonstrations

This directory is a collection of before and after images which
demonstrate what Wbhiteboarder can do.

Click on the following button to run Whiteboarder on Colab:

<a href="https://colab.research.google.com/github/JohnTigue/whiteboarder/blob/master/whiteboarder.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" width="20%" /></a>


### Pipeline #1: rolling ball background removal, CLAHE, then manually thresholded

```python
backgroundless_img, background = subtract_background_rolling_ball(grayed_input_image, 
                                 30, light_background=True,
                                 use_paraboloid=False, do_presmooth=True)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
eqaulized_img = clahe.apply(backgroundless_img)
cv2_imshow(eqaulized_img)

foreground_mask = eqaulized_img < 220
foreground_mask = foreground_mask.astype(np.uint8)*255
masked_image = np.copy(input_color_image)
masked_image[~foreground_mask] = [255, 255, 255]
```

touch_of_orange.jpg:  
<img src="https://johntigue.github.io/whiteboarder/demo/touch_of_orange.jpg" width="90%"/>

red_kneecap.jpg:  
<img src="https://johntigue.github.io/whiteboarder/demo/red_kneecap.jpg" width="90%"/>






