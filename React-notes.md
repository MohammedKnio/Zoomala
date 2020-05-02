# Option 1
`npx create-react-app <your-app-name>`
> If fails, try: `npm -g uninstall create-react-app` then `npx create-react-app <your-app-name>`

# Option 2
`npm init react-app <your-app-name>`

# Option 3
`package.json`:
```
{
  "name": "your-app-name",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^4.2.4",
    "@testing-library/react": "^9.4.0",
    "@testing-library/user-event": "^7.2.1",
    "react": "^16.12.0",
    "react-dom": "^16.12.0",
    "react-scripts": "3.3.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": "react-app"
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
```
Then `npm install`

# Option 4 (using yarm)

```
yarn create react-app my-app
```


```