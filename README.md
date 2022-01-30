# iQuHack 2022: Quantum Key Distribution Library

## Presentation

Our presentation can be found {here}(https://1drv.ms/p/s!AhmabPzKf3o1hbgXwCDZUexX_k4nCg?e=cwiiCY)

## Team: TeamName

Nils, Stefan, Paul, Tobias

## Abstract

Secure messaging is important in multiple sectors. With the rise of quantum computers,
the only way to ensure fully encrypted messaging is to use Quantum Key Distribution. 
Our library implements a modified version of the BB84 protocol on a Quantum Inspire system.
It also offers the framework for two parties to connect to our interface and exchange messages.
We also included a quantum-based random number generator for truly random numbers and a quantum-secure error check 
by comparison of two hash-functions.

## Details About the Implementation
The classical communication was implemented in python while the quantum information channels 
were implemented with cQASM and run on the Quantum inspire platform.


The resulting keys can be compared publicly using a quantum-safe hash function such as sha3-512.
If they match, the key exchange was successful, if they do not match, an error occurred (most likely) in the quantum algorithm, so a re-run is necessary, which our code handles automatically, up to 10 tries.

Once the key hash functions match, a secure connection can be established. We used a symmetric XOR encryption of the message with an elongated key.
The receiving party can then decrypt the message using the same XOR function.

This procedure can be used in any data transfer application, from email to messenger app, as long as a series of qubits can be exchanged between the communicating parties.
Our journalist can now transmit the critical insider information safely.


## Our personal experience

We all really enjoyed the event and had a lot of fun coding together and 
discussing concepts of quantum technology. Besides learning hard skills like Quantum
Key Distribution, we also learned how to properly set up and manage a collaborative project.
It was an enrichment to work in a team with members in multiple countries, so that iQuHack 2022 let us grow not
only as researchers but also as a team.


## Date
January 30, 2022