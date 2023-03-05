from PIL import Image  

images = [Image.open("/mnt/D/Upwork/trials/" + f)
    for f in ["med1.jpg", "med2.jpg", "med3.jpg", "autumn.tif"]]

pdf_path = "/mnt/D/Upwork/trials/pdftest.pdf"
    
images[0].save(pdf_path, "PDF" ,resolution=80.0, save_all=True, append_images=images[1:])
