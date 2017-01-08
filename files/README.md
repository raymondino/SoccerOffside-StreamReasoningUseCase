This directory contains the ontology and the streaming data.

We modularize the overall soccer offside ontology into three sub-ontologies: the individual ontology that encodes the specific match information such as teams and players in each team; the offside offence ontology that concentrates on the offside offence detection from the streaming data; and the domain literate ontology that focuses on filtering out offside-irrelevant data from the streaming data.

# Ontologies' Conceptual Models

![alt text](http://i.imgur.com/vZ3DY9x.png "soccer-offside ontology")

This figure shows the major classes and relations in order to describe the offside offence. When developing this ontology, we use [10] as the text corpus to extract a list of the offside relevant terms. The term list was then carefully examined and curated to create a conceptual model, which was refined and extended to create the offside offence ontology. In a soccer game, usually the player who is touching the ball is considered to be an attacker, along with his teammates. We use this to model the player who touches the ball as BallLastToucher, and the attackers as Attacker. An Attacker can either be the BallLastToucher or (hasTeammate some BallLastToucher). A Defender is defined as (Player and (playsAgainst some Attacker)), where playsAgainst is a symmetric property chain as (isOpponentOf o hasTeammate). Instead of manually labeling the competing relation (isOpponentOf) for each pair of opponent players, leveraging this property chain and a reasoner, the playsAgainst relationships are automatically established, which saves lots of tedious work, keeps a compact ontology and shows the value of the semantics. SecondLastDefender is one of the key concepts to define soccer offside, which is the subclass of both SecondLastPlayer and Defender. We directly annotate a player as SecondLastPlayer for each team by selecting the player who is the second-nearest to his own goal line among his team. This is to reflect the real world scenario that the assistant referee should always keep up with the second last player of his assigned half. The ball being played is an InFieldBall, whereas the other balls are BackupBall. When a player is classified as an Attacker, and isNearerToDefenderGoalLineThan both SecondLastDefender and InFieldBall, he is further classified as PlayerInOffsidePosition. If a player touches the ball or challenges an opponent, he is classified as PlayerInvolvedInActivePlay. Thus, according to the definition of offside offence, when a player is classified as both PlayerInOffsidePosition and PlayerInvolvedInActivePlay, he, who is therefore classified as PlayerCommitsOffsideOffence, commits the offside offence.

![alt text](http://i.imgur.com/hIjID1E.png "domain literate ontology")

This figure illustrates the domain literate ontology. This use case is scoped to answer the question of who commits an offside offence. If a data item does not contain offside offence information, there is no need to execute the query on it. The purpose of this ontology module is to identify and eliminate irrelevant data by leveraging semantics to ask another question (an example is in Listing 2) of what the offside irrelevant positions are prior to execution of the offside query. For the data set of this use case, all ball positions, referee positions, goalkeeper glove positions and player’s positions are present. In this ontology, glove’s position GlovePosition, referee’s position RefereePosition, back up balls’ positions BackupBallPosition, positions of defenders who are not the second last player NotSecondLastDefenderPosition, positions of attackers who are in their own half (owl:intersectionOf (AttackerPosition and OwnHalfPosition)) are all offside irrelevant positions OffsideIrrelevantPosition.

![alt text](http://i.imgur.com/woNkBeF.png "instance ontology")

For the purpose of illustration, we draw three players from each team in this Figure. All of the player individuals have a type of Player, which is a concept in the offside offence ontology. hasTeam is a functional property with a domain of Player and a range of Team, while both hasTeammate and isOpponentOf are symmetric properties with Player as their domain and range. Further, hasTeammate is transitive, meaning that a player can be his own teammate. isOpponentOf is encoded only between two goalkeepers.

# Streaming Data

In data/ folder there 20 segment of streaming data from the DEBS2013 grant challenge. These data will be read by the system to check if there is an offside offence during that data set.

# Benchmark Result

Benchmark results will be generated in the files/ folder as system runs. Also you can refer to ../benchmarks/ folder for all the benchmark records