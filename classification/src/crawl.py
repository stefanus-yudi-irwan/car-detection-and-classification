"""Script for crawling image data for
    classification
"""
import os
import sys
import glob
import logging
from pathlib import Path
from icrawler.builtin import BingImageCrawler

# set root directory
sys.path.append(str(Path(__file__).resolve().parents[2]))
from utils import logger

class ImageCrawler:
    """a class to crawl image 
       using Bing Image crawler
    """
    def __init__(self, output_dir: str) -> None:
        """class initialization
        Args:
            output_dir (str): 
                directory of crawled data be stored
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.class_logger = logger.Logger(script_file="ImageCrawler",
                                          log_dir="../../activity_log",
                                          level="INFO")

    def crawl_image(self, label: str, search_keywords: str, num_image: int) -> None:
        """method to request image, number of image and 
           label the data in a folder
        Args:
            label (str): 
                label of the image (will be stored as folder)
            search_keywords (str):
                keyword will be used to search image in internet
            num_image (int):
                number of approximate image will be crawled
        """
        image_folder = os.path.join(self.output_dir, label)
        os.makedirs(image_folder, exist_ok=True)

        self.class_logger.info(f"Crawling image {label}")
        crawler = BingImageCrawler(storage={"root_dir": image_folder})

        bing_logger = logging.getLogger("icrawler")
        for handler in self.class_logger.logger.handlers:
            bing_logger.addHandler(handler)
        bing_logger.setLevel(self.class_logger.logger.level)
        bing_logger.propagate = False

        crawler.crawl(keyword=search_keywords, max_num=num_image)
        self.class_logger.info(f"Crawling image {label} finish")

        # Rename downloaded image
        self.class_logger.info(f"Formating image name inside folder {image_folder}")
        files = sorted(glob.glob(os.path.join(image_folder,"*")))
        for i, file_path in enumerate(files, 1):
            ext = os.path.splitext(file_path)[-1].lower()
            new_name = f"{label}_{i:03d}{ext}"
            new_path = os.path.join(image_folder, new_name)
            os.rename(file_path, new_path)
        self.class_logger.info(f"Formating image name inside folder {image_folder} finish")

if __name__ == "__main__":

    # Define car categories and number of images
    car_categories = [
        {"label": "bajaj", "keywords": "Gambar Bajaj di Indonesia", "num_images": 200},
        {"label": "double_cabin", "keywords": "Gambar Mobil double cabin di Indonesia", "num_images": 200},
        {"label": "jeep", "keywords": "Gambar Mobil jeep di Indonesia", "num_images": 200},
        {"label": "bus", "keywords": "Gambar Mobil Bus di Indonesia", "num_images": 200},
        {"label": "hatchback", "keywords": "Gambar Mobil Hatchback di Indonesia", "num_images": 200},
        {"label": "minivan", "keywords": "Gambar Mobil minivan di Indonesia", "num_images": 200},
        {"label": "mpv", "keywords": "Gambar Mobil MPV di Indonesia", "num_images": 200},
        {"label": "pickup", "keywords": "Gambar Mobil Pickup di Indonesia", "num_images": 200},
        {"label": "sedan", "keywords": "Gambar Mobil Sedan di Indonesia", "num_images": 200},
        {"label": "suv", "keywords": "Gambar Mobil SUV di Indonesia", "num_images": 200},
        {"label": "truck", "keywords": "Gambar Mobil Truck di Indonesia", "num_images": 200},
    ]

    # Output folder
    OUTPUT_DIR = "../data/raw"

    # Initialize class
    imageCrawler = ImageCrawler(output_dir=OUTPUT_DIR)
    for data in car_categories:
        imageCrawler.crawl_image(label=data['label'],
                                 search_keywords=data['keywords'],
                                 num_image=data['num_images'])
