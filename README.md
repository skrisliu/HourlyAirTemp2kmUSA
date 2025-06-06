# HourlyAirTemp2kmUSA

**Uncertainty-Aware Hourly Air Temperature Mapping at 2 km Resolution via Physics-Guided Deep Learning**  
**Shengjie Kris Liu**  
Email: [skrisliu@gmail.com](mailto:skrisliu@gmail.com)  
GitHub URL: [https://github.com/skrisliu/HourlyAirTemp2kmUSA](https://github.com/skrisliu/HourlyAirTemp2kmUSA)

This repository hosts the dataset and code accompanying our study on high-resolution, hourly near-surface air temperature mapping across the Contiguous United States (CONUS) from 2018 to 2024. The approach integrates physics-guided deep learning with uncertainty quantification.

---

## 📦 Dataset

- **Description:** Hourly near-surface air temperature data at 2 km spatial resolution, covering the Contiguous United States (CONUS), for the years 2018–2024.  
- **Download:** [Zenodo DOI: 10.5281/zenodo.15252812](https://doi.org/10.5281/zenodo.15252812)

> ⚠️ **Note:** This dataset includes the **mean prediction** of the target variable. Due to the 200GB storage limit on Zenodo, the **upper and lower bounds of the predictive uncertainty** are not included here.  
> However, a sample of the uncertainty data for one representative year (2018, ~35GB) is available at [https://osf.io/2x7nt/files/osfstorage](https://osf.io/2x7nt/files/osfstorage).  
> For access to the complete uncertainty dataset (2018–2024), please contact the author directly.


---

## 🧪 Code and Visualization

To visualize the dataset, use the provided script:

- [`visual.py`](https://github.com/skrisliu/HourlyAirTemp2kmUSA/blob/main/visual.py): Load and render hourly temperature data within a specific day with basic animations.

---

## 🖼️ Preview

### February 11, 2018  
![Near-Surface Air Temperature on 2018-02-11](at2018042b.gif)

### July 19, 2018  
![Near-Surface Air Temperature on 2018-07-19](at2018200b.gif)

---

## 📄 How to Cite

If you use this dataset or code, please cite the following:

**📙 Dataset:**
```bibtex
@dataset{liu_2025_15252813,
  author       = {Liu, Shengjie},
  title        = {All-Weather Hourly Near-Surface Air Temperature 2
                   km United States 2018-2024
                  },
  month        = may,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v0.1},
  doi          = {10.5281/zenodo.15252813},
  url          = {https://doi.org/10.5281/zenodo.15252813},
}
```

**📙 Paper:**
```bibtex
@article{Liu2025uncertainty,
  author  = {Liu, Shengjie Kris and Wang, Siqin and Zhang, Lu},
  title   = {Uncertainty-Aware Hourly Air Temperature Mapping at 2 km Resolution via Physics-Guided Deep Learning},
  journal = {forthcoming},
  year    = {2025}
}
```

---

## 📜 License

© 2025 Shengjie Kris Liu. This dataset is licensed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)


