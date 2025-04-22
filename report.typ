CMSE202 SECTION 3 GALACTIC ASTROPHYSICS PROJECT
TEMPERATURE PROFILES OF SPIRAL GALAXIES FROM OPTICAL IMAGES
//
A REPORT
ARTEMIY FILIPPOV, OWEN TORMALA, JACK UTEG, AND RYAN YU

ABSTRACT
To study galactic temperature profiles, we develop a novel analysis pipeline to process spiral galaxy images from the DECaLS Galaxy10 dataset.
We apply image segmentation, masking, and compute for each pixel in the selection of the galactic a color temperature, from which we compute a real temperature.
We proceed to plot the resultant temperature profiles and we find a general trend consistent with the typical understanding of galactic center environments being denser and more energetic than the disk, however we also identify some galaxies which may suggest active star formation in the spiral arms.

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
The analysis of effective temperature profiles across a diverse sample of galaxies reveals several key insights into their thermal structure. We observe a trend in many profiles of a gradual decrease in effective temperature with increasing radial distance from the galaxy center.
This is consistent with theoretical expectations, as stellar populations in the central bulge tend to be hotter and denser than those in the outer regions.

Nevertheless many profiles show deviations from this idealized gradient.
Many galaxies exhibit sharp spikes in temperature at large radii, consistent with artifacts caused by noise amplification in the outermost bins or contamination from bright, foreground stars, background galaxies, or artifacts.
These fluctuations may also stem from limitations in masking accuracy, particularly in irregularly-shaped spiral galaxies.

In galaxies with smoother profiles, a central peak followed by a steady decline reinforces the notion of younger, hotter stellar populations dominating the inner regions.
Conversely, galaxies with flatter or even increasing outer temperature profiles may indicate active star formation in their disks or spiral arms.
A future refinement of this procedure could involve adaptive radial binning, improved masking, or multi-band spectral fitting to enhance the stability and astrophysical reliability of the extracted temperature gradients.