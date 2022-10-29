# File Catalog
The aggregated CESM-LENS data and our simulated realizations from differnt models are provided in this folder.

- annual_global.npz: CESM-LENS global annual temperature data
    - Dimension: 95 (years, 2006-2100) * 35 (runs)
    - Code for loading data:
        ```
        import numpy as np
        data = np.load('annual_global.npz')
        temp = data['temp']
        ```
        
- simulated_model1.npz: our simulated global annual temperature by Model 1
    - Dimension: 95 (years, 2006-2100) * 35 (runs)
    - Code for loading data:
        ```
        import numpy as np
        data = np.load('simulated_model1.npz')
        simulated = data['simulated']
        ```
        
- annual_regional.npz: CESM-LENS regional annual temperature data
    - Dimension: 58 (regions) * 95 (years, 2006-2100) * 35 (runs)
    - Code for loading data:
        ```
        import numpy as np
        data = np.load('annual_regional.npz')
        regionTemp = data['regionTemp']
        ```
        
- simulated_model2.npz: our simulated global annual temperature by Model 2
    - Dimension: 58 (regions) * 95 (years, 2006-2100) * 35 (runs)
    - Code for loading data:
        ```
        import numpy as np
        data = np.load('simulated_model2.npz')
        simulated = data['simulated']
        ```

- monthly_regional.npz: CESM-LENS regional monthly temperature data
    - Dimension: 58 (regions) * 1140 (months, 2006.1-2100.12) * 35 (runs)
    - Code for loading data:
        ```
        import numpy as np
        data = np.load('monthly_regional.npz')
        regionTemp = data['regionTemp']
        ```
        
- simulated_model3.npz: our simulated regional monthly temperature by Model 3
    - Dimension: 58 (regions) * 1140 (months, 2006.1-2100.12) * 35 (runs)
    - Code for loading data:
        ```
        import numpy as np
        data = np.load('simulated_model3.npz')
        simulated = data['simulated']
        ```
        
# What are not provided
The gridded data is too large to put on GitHub. The raw CESM-LENS data can be obtained from https://www.cesm.ucar.edu/projects/community-projects/LENS/data-sets.html