CMSE202 SECTION 3 GALACTIC ASTROPHYSICS PROJECT
A REPORT
ARTEMIY FILIPPOV, OWEN TORMALA, JACK UTEG, AND RYAN YU

ABSTRACT
To study galactic temperature profiles, we develop a novel analysis pipeline to process spiral galaxy images from the DECaLS Galaxy10 dataset.
We apply image segmentation, masking, and compute for each pixel in the selection of the galactic a color temperature, from which we compute a real temperature.
We attempt to plot this temperature as a function of radius, however due to the mosaic background subtraction performed on the original dataset the resultant temperature profiles are not formed properly and often have gaps, interpreted as a nominally negative absolute temperature, suggesting that this is indeed a great difficulty.
Nevertheless, we believe the methods used would be successful if applied to a more fortunate dataset, and we therefore consider the system a success.

SECTION I: MOTIVATION AND PURPOSE
Spiral galaxy dynamics are typically observed to follow flat rotation curves, typically interpreted to be compatible with a uniformly-distributed dark matter.
The visible distributed matter is understood to be primarily stellar matter.
This visible matter mostly therefore emits light according to a black body, whence we may apply the Planck radiation laws to compute from a difference in color in different wavebands, an approximate color temperature; and from that compute a representative surface temperature of the pixel.
From this conceptual exercise, observing the distribution of stellar matter derived by broadband surface brightness, we derive a question to answer: "In spiral galaxies, how does temperature vary by radial distance from the center of said galaxy?"

SECTION II: DEVELOPMENT AND METHODS
Our integrated pipeline was the first part of the project designed.
To facilitate simultaneous development without requiring any one part depend on any other, this pipeline was originally designed to operate on dummy data.
Thus, any one part can be tested within the full pipeline simply by passing to it dummy data -- this dummy data can easily be checked for correctness.
This type of modular design also permits unit testing.
That is to say, each module can be tested entirely on its own and verified to be working entirely on its own.
This resulted in a rapid development phase where each module was developed, tested, and integrated into the pipeline by each developer over a very short period of time.

To examine now the methods used we consider the problem itself: Each of three sky images (for each wave band provided) is to be taken, and the core of a radially-symmetric galaxy identified and selected from this image.
Combining the three waveband images shall then be computed a temperature for each pixel, which may then be unwrapped and converted by radius for each pixel into a single averaged temperature profile for the galaxy, by radius.

Each of these problems requires an individual solution:
For selecting the galaxy from the sky images, we apply image segmentation from the Photutils module.
Masking my be done simply by applying a radius from the segmented image.
Unwrapping may then apply the techniques of a polar coordinate transformation, and the computation of temperature is relies on an empirical correlation of parameters to apply to a modified form of the blackbody radiation laws.

SECTION III: RESULTS AND DISCUSSION
Following development we proceed with an application of the finished pipeline to random data selected from the idea set of galaxies from the DECaLS dataset.
Unfortunately we discovered promptly an issue, where the computed (Kelvin) temperature is negative.
This is necessarily non-physical.

We proceeded with a rudimentary cause analysis.
The ultimate cause appears to have been, unfortunately, the background subtraction pre-applied to the dataset, to remove the brightness of the sky from these images.
A standard method to do so generates a grid upon the image; some fraction of the baseline of each cell is subtracted from the contents thereof.
This method may be applied without such consequence to data to be used for imaging purposes (as is the case of this dataset), but for extended sources, it will disrupt the photometry of each pixel.
The resultant damaged photometry was then scaled to fit in a uint8, which further compressed it; and we are unable to therefore recover the original pixel values.
As such, we contest our results are defective not because of our pipeline, but in spite of it -- a better dataset, perhaps of higher resolution (such that the background subtraction mosaic shall be a smaller portion of the spatial distribution of the targets themselves -- and we therefore, despite the lack of any meaningful answer to the original question, we nevertheless fully believe our method itself to be successful, limited only by the data available to such a cause.