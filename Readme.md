# Whiteboarder

<img src="https://johntigue.github.io/whiteboarder/images/headers/four_very_white_colored_caps.jpg" width="100%"/>

MIT licensed code for processing whiteboard images.

See demos directory for more.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JohnTigue/whiteboarder/blob/master/whiteboarder.ipynb)


## Demo

### 1. First pipeline

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

red_kneecap.jpg:  
<img src="https://johntigue.github.io/whiteboarder/demo/red_kneecap.input.jpg" width="45%"/><img src="https://johntigue.github.io/whiteboarder/demo/red_kneecap.output_1.jpg" width="45%"/>


carrot_top.jpg:  
<img src="https://johntigue.github.io/whiteboarder/demo/carrot_top.input.jpg" width="45%"/><img src="https://johntigue.github.io/whiteboarder/demo/carrot_top.output_1.jpg" width="45%"/>


 
