## REQUIREMENTS
- Design Unix File Search API to search file with different arguments as "extension", "name", "size" ...
- The design should be maintainable to add new contraints.
- AND | OR Conditionals

### what we need to do
- Consider file and directory structure as n-ary tree.
- Your root path is the starting node. All the files in system are leaf nodes and all the directories are n-ary sub trees.
- Perform DFS/BFS starting from root and visit all files.
- If a file satisfies "find" requirement then add it to result
