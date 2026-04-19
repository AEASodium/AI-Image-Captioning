# AI Image Captioning Application (BLIP)

A local-first AI application that generates descriptive captions for images using the BLIP (Bootstrapping Language-Image Pre-training) model. This project was developed as part of the IBM Generative AI Engineering curriculum.

## 🚀 Key Milestones & Troubleshooting
This project involved significant environment-specific debugging to ensure local stability on Windows/WSL2:

* **Environment Integration:** Successfully migrated from cloud-based environments to a local **Miniconda/VS Code** setup on a high-performance workstation (D: Drive).
* **Pipeline Optimization:** Resolved a library-specific `KeyError` by migrating the `transformers` pipeline task from `image-to-text` to `image-text-to-text`.
* **UI Modernization:** Fixed Gradio 4.0+ compatibility issues by updating interface parameters (e.g., `flagging_mode`).
* **Hardware Efficiency:** Implemented CPU-optimized PyTorch wheels to ensure smooth inference on an Intel i5 processor without requiring dedicated GPU VRAM.
* **Containerization Readiness:** Authored a production-ready `Dockerfile` optimized for serverless deployment platforms like IBM Code Engine.

## 🛠️ Tech Stack
* **Model:** `Salesforce/blip-image-captioning-base`
* **Frameworks:** Transformers, Gradio, PyTorch, Pillow
* **Environment:** Python 3.10+, Miniconda, Docker (Architecture Ready)

## 📸 Local Verification
The application has been verified with diverse imagery, including astronomical data (Saturn) and culinary scenes, successfully producing accurate linguistic descriptions.