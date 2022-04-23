# National Resident Matching Programme
UID: 202204131426
Tags: #🌱 
Links: [[Strategic Thinking]] [[Marriage problems (Game Theory)]]

Med student internships used to be regulated by market forces. i.e. Hospitals would try to compete for interns by sending offers as early as possible, at times even up to two years before the actual residency training. Some of these offers are time-sensitive, known as "exploding offers", which expires when the phone call ends. 
- This results in an unideal situation for both the hospitals and the residents-to-be
	- For the former, they cannot ensure the quality of the students that early on, but are left with no choice but to secure the candidates early
	- For the latter, they are unable to make the best choice, since a better deal may come along the way, or not.
As a result, the NRMP was set up, and chooses to use the Deferred Acceptance Algorithm (aka. the Gale-Shapley Algorithm) which is the algorithm explored in [[Marriage problems (Game Theory)]].

### Optimality of proposing side
By using the DA algorithm, the proposing side maximises their welfare across all possible stable matchings, while the accepting side's most preferred stable matching would be the least preferred for the proposing side.

Initially, the NRMP uses a hospital-proposing algorithm. However, intending to optimise applicant (i.e., residents-to-be) welfare, the NRMP switched to an applicant-proposing system after Gale and Shapely's findings.