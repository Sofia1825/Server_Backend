# Server Backend - Huerta Comunitaria

API REST desarrollada con Django y Django REST Framework para la gestión de agricultores y cultivos.

## Endpoints disponibles
- `GET / POST / PUT / DELETE` -> `/api/agricultores/`
- `GET / POST / PUT / DELETE` -> `/api/cultivos/`

## Ejecución local
1. Activar entorno virtual: `source venv/Scripts/activate`
2. Aplicar migraciones: `python manage.py migrate`
3. Iniciar servidor: `python manage.py runserver`

Note: This will impact Vite dev & build performances.
You can also try [the experimental native React Compiler support in plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md#rust-react-compiler) by using `compiler: true` in the plugin options instead of using the Babel plugin.

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
