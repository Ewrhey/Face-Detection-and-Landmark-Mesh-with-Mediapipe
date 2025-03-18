Eng description:
# Face Detection and Landmark Mesh with Mediapipe

This project demonstrates face detection and facial landmark mesh generation using **Mediapipe**, a cross-platform framework for building multimodal applied machine learning pipelines. It includes face detection, bounding box drawing, and drawing facial landmarks (mesh) on faces within an image.

## Features

- **Face Detection**: The model detects faces in images using the `FaceDetection` model from Mediapipe.
- **Face Mesh**: Draws facial landmarks (key facial features) using the `FaceMesh` model from Mediapipe.
- **Face Identification**: Assigns a unique ID to each detected face and labels it.
- **Support for Multiple Faces**: Detects and processes multiple faces in a single image (up to 10 faces).
- **Real-time Display**: Visualizes the results with bounding boxes around faces and facial landmarks on the image.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Mediapipe (`mediapipe`)
- Matplotlib (for displaying images)

## Installation

To install the necessary dependencies, run:

```bash
pip install opencv-python mediapipe matplotlib
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Face-Detection-and-Mesh.git
cd Face-Detection-and-Mesh
```

2. Run the script:

```bash
python face_detection_mesh.py
```

3. The program will prompt you to input an image number (e.g., `1`, `2`, etc.). It expects images named `input_image1.jpg`, `input_image2.jpg`, etc., in the same directory.
4. The script will display the images with bounding boxes around detected faces and facial landmarks drawn on them.

## Code Walkthrough

- **Face Detection**: The face detection is performed using the `FaceDetection` model from Mediapipe. A bounding box is drawn around each detected face.
- **Face Mesh Generation**: The `FaceMesh` model detects 468 landmarks on each detected face. These landmarks are drawn on the image, connecting key points to form a mesh of the face's structure.
- **Face Labeling**: Each detected face is assigned a unique ID (e.g., "Face 1", "Face 2", etc.), making it easier to distinguish between multiple faces in an image.

## Limitations

- The script assumes that images are named in a sequential manner (e.g., `input_image1.jpg`, `input_image2.jpg`, etc.).
- The model is set to detect a maximum of 10 faces per image.
- The face mesh model might not work well with extreme facial poses or occlusions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Ru description:

---

# Обнаружение лиц и сетевая модель с Mediapipe

Этот проект демонстрирует обнаружение лиц и генерацию сетки лицевых ориентиров с использованием **Mediapipe** — кросс-платформенной фреймворк для создания многомодальных машинно-обучающих приложений. Проект включает в себя обнаружение лиц, рисование ограничивающих рамок и нанесение лицевых ориентиров (сетки) на лица в изображениях.

## Особенности

- **Обнаружение лиц**: Модель обнаруживает лица на изображениях с помощью модели `FaceDetection` из Mediapipe.
- **Лицевая сетка**: Рисует лицевые ориентиры (ключевые черты лица) с использованием модели `FaceMesh` из Mediapipe.
- **Нумерация лиц**: Каждому обнаруженному лицу присваивается уникальный идентификатор, и оно помечается на изображении.
- **Поддержка нескольких лиц**: Обнаруживает и обрабатывает несколько лиц на одном изображении (до 10 лиц).
- **Отображение в реальном времени**: Визуализирует результаты с ограничивающими рамками вокруг лиц и рисует лицевые ориентиры на изображении.

## Требования

- Python 3.x
- OpenCV (`cv2`)
- Mediapipe (`mediapipe`)
- Matplotlib (для отображения изображений)

## Установка

Для установки необходимых зависимостей выполните команду:

```bash
pip install opencv-python mediapipe matplotlib
```

## Использование

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/Face-Detection-and-Mesh.git
cd Face-Detection-and-Mesh
```

2. Запустите скрипт:

```bash
python face_detection_mesh.py
```

3. Программа попросит вас ввести номер изображения (например, `1`, `2` и т.д.). Ожидаются изображения с именами `input_image1.jpg`, `input_image2.jpg` и т.д. в той же директории.
4. Скрипт отобразит изображения с ограничивающими рамками вокруг обнаруженных лиц и с нанесёнными лицевыми ориентирами.

## Обзор кода

- **Обнаружение лиц**: Обнаружение лиц осуществляется с помощью модели `FaceDetection` из Mediapipe. Для каждого обнаруженного лица рисуется ограничивающая рамка.
- **Генерация лицевой сетки**: Модель `FaceMesh` обнаруживает 468 ориентиров на каждом обнаруженном лице. Эти ориентиры рисуются на изображении, соединяя ключевые точки, чтобы сформировать сетку структуры лица.
- **Нумерация лиц**: Каждому обнаруженному лицу присваивается уникальный идентификатор (например, "Лицо 1", "Лицо 2" и т.д.), что упрощает различение нескольких лиц на изображении.

## Пример

Пример того, как будет выглядеть изображение после обработки:

![example](example_image.jpg)

## Ограничения

- Скрипт предполагает, что изображения имеют последовательные имена (например, `input_image1.jpg`, `input_image2.jpg` и т.д.).
- Модель настроена на обнаружение максимума 10 лиц на одном изображении.
- Модель лицевой сетки может работать не так точно при экстремальных позах лиц или их частичной блокировке.

## Лицензия

Этот проект распространяется под лицензией MIT — см. файл [LICENSE](LICENSE) для подробностей.
