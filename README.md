# HourlyAirTemp2kmUSA

**Uncertainty-Aware Hourly Air Temperature Mapping at 2 km Resolution via Physics-Guided Deep Learning**  
Shengjie Liu<sup>1*</sup>  
Email: [skrisliu@gmail.com](mailto:skrisliu@gmail.com)

This repository hosts the dataset and code accompanying our study on high-resolution, hourly near-surface air temperature mapping across the Contiguous United States (CONUS) from 2018 to 2024. The approach integrates physics-informed deep learning with uncertainty quantification.

GitHub URL: [https://github.com/skrisliu/HourlyAirTemp2kmUSA](https://github.com/skrisliu/HourlyAirTemp2kmUSA)

---

## 📦 Dataset

- **Description:** Hourly near-surface air temperature data at 2 km spatial resolution, covering the Contiguous United States (CONUS), for the years 2018–2024.  
- **Download:** [Zenodo DOI: 10.5281/zenodo.15252812](https://doi.org/10.5281/zenodo.15252812)

> ⚠️ **Note:** Due to the 200GB storage limit on Zenodo, this dataset **does not include the lower and upper bounds of the predictive uncertainty**. A separate link for one representative year (~35GB) will be provided here by **June 6**. For access to the full uncertainty data (2018–2024), please contact the author directly.

---

## 🧪 Code and Visualization

To visualize the dataset, use the provided script:
- [`visual.py`](https://github.com/skrisliu/HourlyAirTemp2kmUSA/blob/main/visual.py): Load and render daily or hourly temperature rasters with basic animations.

---

## 🖼️ Preview

### February 11, 2018
![Near-Surface Air Temperature on 2018-02-11](at2018042b.gif)

### July 9, 2018
![Near-Surface Air Temperature on 2018-07-09](at2018200b.gif)

---

## 📄 How to Cite

If you use this dataset or code, please cite the following:

**📘 Dataset:**
@dataset{Liu2025HourlyAirTemp2kmUSA,
  author       = {Liu, Shengjie},
  title        = {HourlyAirTemp2kmUSA: Hourly Air Temperature Estimates with Uncertainty at 2 km over the United States (2018–2024)},
  year         = {2024},
  doi          = {10.5281/zenodo.15252812},
  publisher    = {Zenodo},
  url          = {https://doi.org/10.5281/zenodo.15252812}
}

**📙 Paper:**
@article{Liu2025uncertainty,
  author  = {Liu, Shengjie and Wang, Siqin and Zhang, Lu},
  title   = {Uncertainty-Aware Hourly Air Temperature Mapping at 2 km Resolution via Physics-Guided Deep Learning},
  journal = {forthcoming},
  year    = {2025}
}
