# Galaxy Temperature Modelling

This repository is home to an experiment on using multiwavelength optical images to model the temperature profiles of spiral galaxies from the Galaxy10 DECaLS dataset.
Created for a final project in a computer science class, our team is super happy with the implementation of a multi-part project on this scale, even though there were a few problems with the final implementation of the concept which could be improved in the future.

### Concept
The concept of this project was primarily to leverage the size of our team.
With four team members, it was critical to find some structure that would allow all to contribute simultaneously without anyone relying on any other part being completed in any given timeframe.
The result was a framework that uses a pattern similar to dependency injection.
The top-level pipeline was the first part of the project implemented, and then as each subsequent part was written with a matching interface, as they were completed each was merged into the main project.
At the end, following minor integration testing, we were left with an almost! functional project that, if it weren't for a few minor factors, would be compositing plots of spiral galaxy temperature as a function of radius.

### Successes
As a team, developing this project was a joy.
With each team member able to focus entirely on implementing a small but integral part of the project, the entire project was implemented in less than 600 SLOC, and slotting everything together was a very simple process.
Additionaly, because of the modular design, each part could be debugged, tested, and fixed separately.
This resulted in an ergonomic development process that provided exceptional locality of behavior and prevented any module from sprialing with feature creep.
Aditionally, the implementation of each individual part seems to have gone incredibly smoothly, resulting in a tight pipeline that fully processes our data quickly, and it is very easy to understand the whole program thanks to the pipeline and subprocess design.

### More Information
See `report/report.pdf` for a complete report on the development and results of this project.

## Contributors 
- Artemiy Filippov | AttackOnBreakfast
- Owen Tormala     | Tormalao
- Jack Uteg        | HobbitJack
- Ryan Yu          | Ryan-yu2024

## Resources
### Code
Code from https://github.com/wh1tewolfxx/Python-Polar-Unwrap used under Expat/MIT license -- Copyright C Dakota Napierkowski 2022

### Dataset
Galaxy10 DECaLS Dataset: https://github.com/henrysky/Galaxy10

### Theoretical
F. J. Ballesteros 2012 *EPL* 97 34008 https://iopscience.iop.org/article/10.1209/0295-5075/97/34008

### Module Documentation
Astropy Documentation: https://docs.astropy.org/en/stable/index_user_docs.html

h5py Documentation: https://docs.h5py.org/en/stable/index.html

Matplotlib Pyplot Documentation: https://matplotlib.org/stable/api/pyplot_summary.html

Numpy Documentation: https://numpy.org/doc/2.2/user/index.html#user

Photutils Documentation: https://photutils.readthedocs.io/en/stable/index.html

## License
All source code files in this project is licensed under the permissive Expat/MIT license.
See the file LICENSE included in this repository for a full list of terms.
