# Fabriplate

Starting point for using Fabric in an extensible way. ```roles.json``` allows
the developer to extend the utility of Fabric roles to store arbitrary
data.

## Usage

Use ```roles.json``` to store all the data associated with a given role. Note that 
`role` and `hosts` are both required keys.

Invoking `get_role` will return the dictionary associated by the current role.

## Requirements
- Python >= 2.6
- Fabric >= 1.6