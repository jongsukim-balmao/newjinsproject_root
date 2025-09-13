# Simple React dev image; for production, build and serve via nginx or S3/CDN
FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json* yarn.lock* pnpm-lock.yaml* ./
RUN if [ -f yarn.lock ]; then corepack enable && yarn install --frozen-lockfile; \
    elif [ -f pnpm-lock.yaml ]; then corepack enable && pnpm install --frozen-lockfile; \
    else npm ci || npm install; fi
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
