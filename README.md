# ImageRetrieval

Have a look on the image retrieval platform first,

![2018-05-19 10-00-29 1](https://user-images.githubusercontent.com/11582122/40263890-f8dc8d3e-5b4b-11e8-89e4-2c2a20280586.png)

The project is based on django and vgg net. To run the code, we need download the [vgg16 pre-trained model](https://www.cs.toronto.edu/~frossard/vgg16/vgg16_weights.npz) and place it at `SearchImg/SearchImg`.
And then install serveral necessary packages:
```bash
sudo pip3 install tensorflow
sudo pip3 install django
```

After the above prepare, we can simply run the following command and get the image retrieval website:
```bash
python manage.py runserver
```
