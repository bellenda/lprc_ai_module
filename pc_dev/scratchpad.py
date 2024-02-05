from ultralytics import YOLO

#Load a pretrained model
model = YOLO('yolov8n.pt')

#Run inference on the source
results = model(source="retail_stock1.mp4", show=True, conf=0.4, save=True) #generator of Results objects