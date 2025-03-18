import cv2
import mediapipe as mp

# Initialize the models
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Initialize face detection and face mesh models
face_detection = mp_face_detection.FaceDetection(model_selection=1,
                                                 min_detection_confidence=0.7)  # Increased confidence threshold
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=10, refine_landmarks=True,
                                  min_detection_confidence=0.7)

while True:
    # Get the image path from the user input
    imagePath = "input_image" + input("Input number of image or -1 to exit: ") + ".jpg"

    # Exit the loop if the user inputs "-1"
    if imagePath == "input_image-1.jpg":
        break

    # Read the image
    image = cv2.imread(imagePath)

    # Check if the image was loaded correctly
    if image is None:
        print("Sorry,", imagePath, "not found!")
        continue

    # Convert the image to RGB as Mediapipe uses RGB format
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform face detection
    results = face_detection.process(rgb_image)

    # Perform face mesh detection
    mesh_results = face_mesh.process(rgb_image)

    # Draw bounding boxes around detected faces and label them
    if results.detections:
        face_id = 1  # Initialize face counter
        for detection in results.detections:
            # Get bounding box coordinates for the detected face
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape  # Get image dimensions
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

            # Draw rectangle around the face
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Label the face with an ID
            cv2.putText(image, f"Face {face_id}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Draw face mesh landmarks if they are detected
            if mesh_results.multi_face_landmarks:
                for face_landmarks in mesh_results.multi_face_landmarks:
                    mp_drawing.draw_landmarks(
                        image, face_landmarks,
                        connections=mp_face_mesh.FACEMESH_CONTOURS,  # Draw only key facial contours
                        landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1, circle_radius=1),
                        connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1)
                    )
            # Increment the face ID for the next face
            face_id += 1

    # Display the resulting image with bounding boxes and landmarks
    cv2.imshow("Mediapipe Face Detection & Mesh on Group Photo", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
