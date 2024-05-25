# IDSI-Integrated-Drought-Serverity-Index
This is repository for Integrated Drought Severity Index (IDSI) model . IDSI is empirical model given by IWMI.

## Drought
Drought is a temporary weather event that arises from a lack of rainfall over an extended period, relative to the long-term average conditions. The onset of a drought is typically marked by a decrease in precipitation, but over time, it can lead to a reduction in groundwater, soil moisture, and stream flow.

Drought is a complex event that progresses slowly and steadily, making it challenging to identify its commencement. To gain a clearer understanding of the intricacies of drought, national and international organizations have utilized Remote Sensing data. Simple indices such as NDVI, NDWI, and NDSI provide insights into the current state of vegetation and moisture content.

However, these indices are not comparative. To fully comprehend the complexity of drought, it’s essential to use comparative indices and integrate these indices in some way. This approach allows for a more nuanced understanding of drought conditions and their impacts.

## Integrated Drought Severity Index
Droughts are becoming increasingly prevalent worldwide, particularly in South Asia. The International Water Management Institute (IWMI), located in Colombo, Sri Lanka, conducts scientific research focusing on the sustainable utilization of water and land resources in developing nations.

Drought is a complex event that progresses gradually and steadily, making its onset challenging to detect. Simple indices such as the Normalized Difference Vegetation Index (NDVI), Normalized Difference Water Index (NDWI), and Normalized Difference Snow Index (NDSI) provide indications of the current state of vegetation and moisture content.

The IWMI, in collaboration with other research institutes like the Indian Council of Agricultural Research (ICAR), has developed the Integrated Drought Severity Index (IDSI). This index combines three other indices: the Temperature Condition Index (TCI), Precipitation Condition Index (PCI), and Vegetation Condition Index (VCI).


![IDSI_1](https://github.com/shivaprakash23/IDSI-Integrated-Drought-Serverity-Index-/assets/13203442/c7615e09-453d-4fc4-9133-461142711244)

Where,
- **LST**: Land Surface Temperature
- **NDVI**: Normalized Difference Vegetation Index
- **TRMM**: Tropical Rainfall Measurement Mission
- **curr**: Current
- **min**: Minimum
- **max**: Maximum

To generate VCI, PCI, and TCI, we need raster grids that capture the minimum and maximum values over a span of 15 years. These grids should specifically include data for Land Surface Temperature (LST), Normalized Difference Vegetation Index (NDVI), and Tropical Rainfall Measurement Mission (TRMM). The minimum value grid and the maximum value grid for each of these parameters are essential for the calculations. Obtaining the minimum and maximum raster grids constitutes a significant portion of the work, given its time-consuming nature. These grids are crucial for subsequent calculations. Utilizing the minimum, maximum, and current raster grid data, we computed the Vegetation Condition Index (VCI), Temperature Condition Index (TCI), and Precipitation Condition Index (PCI) for monthly data. Specifically, for our study area, VCI, TCI, and PCI were computed for the months of February, March, April, May, June, and July. The resulting monthly data for VCI, TCI, and PCI were then utilized for further analysis and interpretation.

The Month-wise Integrated Drought Severity Index (IDSI) is calculated using a specific formula, resulting in values ranging from 0 to 100. In this context, an IDSI value close to zero indicates an extreme drought condition, while a value near 100 signifies a healthy condition. Following the classification by the International Water Management Institute (IWMI), different ranges of IDSI values correspond to distinct categories, indicating the severity of drought conditions.
These categories could be
- Healthy
- Normal
- Watch
- Stress
- Moderate Drought
- Severe Drought
- Extreme Drought

This categorization helps in understanding and interpreting the severity of drought events, facilitating informed decision-making and management strategies for water resources and agricultural activities.

## IDSI Formula
<img width="419" alt="IDSI_2" src="https://github.com/shivaprakash23/IDSI-Integrated-Drought-Serverity-Index-/assets/13203442/a1c3eaa8-5382-4a00-960b-0bba81eb6e07">




