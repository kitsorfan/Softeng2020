# TL20-template
This is a team project for Software Engineering Lesson of ECE NTUA


Template repository, used for NTUA/ECE Software Engineering, 2020-2021

Το αρχείο αυτό περιέχει οδηγίες για το στήσιμο του git repository που θα
χρησιμοποιήσετε.  Στο τέλος, θα το αντικαταστήσετε με το `README.md` που
θα περιγράφει το δικό σας project.


## Στήσιμο του repository

Αν σας αρκεί να ξεκινήσετε με αυτό το (κενό) template repository και να
προσθέσετε εκεί ό,τι γράψετε, τότε είστε ευτυχισμένοι και έτοιμοι:

```sh
git clone git@github.com:ntua/TL20-nn
```

όπου φυσικά θα αντικαταστήσετε το `nn` με τον αριθμό της ομάδας σας.

Αν είχατε ήδη αρχίσει να δουλεύετε σε κάποιο δικό σας git repository,
τότε έχετε τις εξής **εναλλακτικές** επιλογές.

> Οι δύο τελευταίες είναι κάπως επικίνδυνες --- διαβάστε πρώτα πώς δουλεύει
> το `git` πριν τις εφαρμόσετε και βεβαιωθείτε ότι καταλαβαίνετε ακριβώς
> τι κάνουν οι εντολές που εκτελείτε.
> Θεωρήστε ότι σας προειδοποιήσαμε και, disclaimer, δεν κάνουμε git support!
> Αν χαλάσετε το repository σας, λυπούμαστε πολύ αλλά είναι δικό σας πρόβλημα...

1.  Να αντιγράψετε τα αρχεία από το δικό σας repository στο παρόν,
    να τα κάνετε `git add`, `git commit` και `git push`.  Αυτή είναι
    η απλούστερη λύση, αλλά έχει το μειονέκτημα ότι **θα χάσετε το
    commit history** από το δικό σας repository.

2.  Να μεταφέρετε το δικό σας repository **σβήνοντας** τα περιεχόμενα
    του παρόντος.  Ξεκινώντας από ένα **clean** working directory του
    δικού σας υπάρχοντος repository:

    ```sh
    git remote add official git@github.com:ntua/TL20-nn.git
    git push -f official master
    ```

    Αν έχετε και άλλα branches, π.χ. κάποιο που λέγεται `other-branch`,
    μπορείτε να τα κάνετε `git push` και εκείνα.

    ```sh
    git push official other-branch
    ```

    Στη συνέχεια, μπορείτε να κάνετε ένα φρέσκο `git clone` και να δουλεύετε
    στο παρόν repos.

3.  Να μεταφέρετε το history από το δικό σας repository **προσθέτοντας**
    στο παρόν.  Ξεκινώντας από ένα **clean** working directory του δικού
    σας υπάρχοντος repository:

    ```sh
    git remote add official git@github.com:ntua/TL20-nn.git
    git push official master:our-master
    ```

    Αν έχετε και άλλα branches, π.χ. κάποιο που λέγεται `other-branch`,
    μπορείτε να τα κάνετε `git push` και εκείνα.

    ```sh
    git push official other-branch
    ```

    Στη συνέχεια, μπορείτε να κάνετε ένα φρέσκο `git clone` και να δουλεύετε
    στο παρόν repos.  Το δικό σας `master` branch θα λέγεται `our-master`.
    Μπορείτε να το κάνετε rebase πάνω στο `master` του παρόντος repository,
    με την παραπάνω διαδικασία:

    ```sh
    git checkout our-master
    git checkout -b rebased-master
    git rebase origin/master
    ```

    Αναλόγως αν έχετε ακολουθήσει το directory structure και πόσο τυχεροί
    είστε, είναι πιθανό να χρειαστεί να επιλύσετε κάποια conflicts.

    Στη συνέχεια, αν το παραπάνω rebase τελειώσει επιτυχώς, μπορείτε να
    μεταφέρετε το αποτέλεσμα στο master branch και να ξεφορτωθείτε τα
    πλέον άχρηστα branches

    ```sh
    git checkout master
    git merge rebased-master
    git branch -d rebased-master
    git branch -D our-master
    ```


## Directory structure

Δομήστε τα παραδοτέα σας στους παρακάτω φακέλους όπως φαίνεται στην
εκφώνηση της εργασίας.

**/documentation**
- έγγραφα τεκμηρίωσης και διαγράμματα

**/back-end**
- πηγαίος κώδικας και έλεγχοι του back-end της εφαρμογής

**/cli-client**
- πηγαίος κώδικας και έλεγχοι του CLI client

**/front-end**
- πηγαίος κώδικας και έλεγχοι του front-end της εφαρμογής
