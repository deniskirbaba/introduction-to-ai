# Recognition of human activity based on data from mobile sensors #

It is necessary to predict human activity by six classes of movements using data from mobile sensors using applied machine learning algorithms:
* Moves in a straight line
* Moves up (for example, going up stairs)
* Moves down (for example, going down stairs)
* Is sitting
* Costs
* Lies

## Dataset Details ##

The dataset contains sensor records from smartphones (accelerometer and gyroscope with a sampling rate of 50 Hz) from 30 participants performing the following actions: walking, walking stairs, walking stairs, sitting, standing and lying. The data was pre-processed using noise filters. The dataset is provided by Jorge L. Reyes-Ortiz.

The features were extracted from the tAcc-XYZ and tGyro-XYZ 3-axis raw signals of the accelerometer and gyroscope. These signals were recorded at a constant frequency of 50 Hz. They were then filtered with a median filter and a 3rd order Butterworth low-pass filter with a frequency of 20 Hz to remove noise. Similarly, the acceleration signal was split into the body acceleration and gravity signals (`tBodyAcc-XYZ` and` tGravityAcc-XYZ`) using another low-pass Butterworth filter with an angular frequency of 0.3 Hz. The linear acceleration of the body and the angular velocity were used to obtain the "jerk" signals - (`tBodyAccJerk-XYZ` and` tBodyGyroJerk-XYZ`). Also, the magnitude of these three-dimensional signals was calculated using the Euclidean norm - (`tBodyAccMag`,` tGravityAccMag`, `tBodyAccJerkMag`,` tBodyGyroMag`, `tBodyGyroJerkMag`).

Finally, a Fast Fourier Transform (FFT) was applied to some of these signals, resulting in `fBodyAcc-XYZ`,` fBodyAccJerk-XYZ`, `fBodyGyro-XYZ`,` fBodyAccJerkMag`, `fBodyGyroMag`, `fBodyGyroJerkMag` (Note the "f" for frequency domain signals).

The set of variables that were evaluated for these signals is as follows:
* mean (): Average value
* std (): Standard deviation
* mad (): Mean absolute deviation
* max (): Largest value in the array
* min (): The smallest value in the array
* sma (): Signal magnitude area
* energy (): A measure of energy. The sum of squares divided by the number of values.
* iqr (): Interquartile range
* entropy (): Signal entropy
* arCoeff (): Autoregressive coefficients with Burg order of 4
correlation (): correlation coefficient between two signals
* maxInds (): the index of the frequency component with the highest value
* meanFreq (): weighted average of the frequency components to obtain the mean frequency
* skewness (): skew of the signal in the frequency domain
* kurtosis (): kurtosis in the frequency domain
* bandsEnergy (): Energy of the frequency range within 64 FFT bins of each window.
* angle (): The angle between vectors.