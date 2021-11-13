# Scibuild

Scibuild is a little build system for automating the process of writing scientific papers. With Scibuild you can build a pipeline for generating results, assembling the results, generating tables and graphs, and injecting them in LaTeX files.

It should be noted that this is a toy project, and is definitely not production-ready. Feel free to mess around.

## How to use

Simply call the script `python3 scibuild.py [path-to-your-scibuild-file]`.

## Example file

The following script defines a paper named "Monte Carlo Method for Estimating Pi" containing a single experiment named "Running MC for a fixed set of parameters".

In this experiment, two variables are defined, `side` and `num_trials`. A python script is then called with the `cmd` command and the two variables are passed as arguments.

This is still very simple, but should give you an idea of what I have in mind.

```sh
paper "Monte Carlo Method for Estimating Pi" {

    experiment "Running MC for a fixed set of parameters" {

        // Defining parameters

        let side = 1.0
        let num_trials = 100

        // Running steps

        cmd("./my-script.py", side, num_trials)

    }

}
```
