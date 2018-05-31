# ia1
codes for artificial intelligence 1 activities

see **ia1-descricao.pdf** [ptbr] 

attention: ugly codes, not refactored nor efficient.

what needs to be done

## q1
- [x] modularize code
- [x] fix presentation stage
- [x] fix dfs (idk why it is not working properly)
- [x] add solutions' depth in every algorithm 
- [ ] add shortest path as solution depth
- [ ] add solutions' path 
    - [ ] dfs, bfs
    - [ ] idfs
- [x] add thread to solve with each algorithm
- [ ] add unit tests

## q2
- [ ] fix forward chaining (no question needed, just get results in facts base)
- [ ] fix back and forward to consider differents antecedents producing one
consequent

# brainstorming

what we need? supposing that the engine inference is ok...

- web interface (django)
- variables/values
    - add, modify, remove, show
    - numeric, univalued, multivalued
- questions (interface)
    - add, modify, remove, show
- rules
    - add, modify, remove, show
    - structure
        - <conective> <atr> <opr> <val>
            - conective: NÃO, E, OU 
            - atr: variable
            - opr: relational oprs
            - val: related to atr
    - premisses
        - <atr> = <val> <confidence deg>
- probabilities?
- objectives
- search tree (explanation func)
- inference engine
    - conjunctions, disjunctions

again:

what are the models?
    atoms
    antecedents
    consequents
    rule

what are the relations?
    rule has one antecedent and consequent
    consequents have one premisse with only one atom (for now)

apps
    chaining
    editor
    explation

what to do really?
    - some erros in models like Rule.__str__ 
    - do I really need that expression has three variables? why not just 'is'
      or 'not is'?
    - the way we add in admin app is not good, but either way I will have to do
      mine
    - OKAY, what:
        - first I have to set model right and test it, please
        - second I have to test chaining methods, please. I need to be okay
          with it to focus on views
        - last focus on views. bigger problem when all the rest is okay
        - 3 days!
    - 
