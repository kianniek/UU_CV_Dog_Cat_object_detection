## 👤 Kian: Data, Evaluation & Augmentation
*Focus: Data integrity, preprocessing, and final performance metrics.*

- [x] **1. Load and Prepare Data** 
    - [x] Perform stratified 80/20 split.
    - [x] Implement image resizing (112x112x3) and bounding box scaling.
    - [x] **Report:** Explain resizing methodology and box transformations.
- [x] **4. Evaluate Performance** 
    - [x] Calculate mAP by varying objectness threshold (0 to 1).
    - [x] Generate Confusion Matrix for the best threshold.
    - [x] **Report:** Discuss performance differences (Train vs. Val vs. Test.
- [ ] **Choice 6: Data Augmentation** 
    - [ ] Implement $\geq 3$ techniques (e.g., color jitter, horizontal flip).
    - [ ] **Report:** Compare mAP results with and without augmentation.
- [ ] **Choice 7: Misdetection Analysis** 
    - [ ] Identify and discuss False Positives/Negatives and cat-dog swaps.

---

## 👤 Vinn: Architecture, Training & Post-Processing
*Focus: Neural network construction, loss functions, and inference logic.*

- [x] **2. Develop the Architecture** 
    - [x] Build the 1M parameter YOLOv1-style model with the specific 5-block structure .
    - [x] Implement the 343-neuron sigmoid output layer.
    - [x] **Report:** Provide architecture summary and motivate activation/pooling choices.
- [x] **3. Train the Model** 
    - [x] Implement the **five YOLOv1 loss components** and their weights.
    - [x] Set up training loop with Early Stopping.
    - [x] **Report:** Document hyperparameters and generate loss component graphs.
- [ ] **Choice 8: Non-Maximum Suppression (NMS)** 
    - [ ] Implement NMS as a post-prediction step (not during training.
    - [ ] **Report:** Compare mAP/Confusion Matrix with and without NMS.
- [x] **Choice 1: Improve Architecture** 
    - [x] Motivate and implement impactful changes (e.g., deeper layers, different kernels).

---

## 🤝 Joint Responsibilities
- [ ] **Weights:** Ensure the final model weights are linked in the report.
- [ ] **Final Polish:** Review the 2–5 page report for consistency and clarity.
