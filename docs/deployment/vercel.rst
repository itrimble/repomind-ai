Vercel Deployment Guide
=======================

This guide covers deploying RepoMind AI to Vercel for production use.

Prerequisites
-------------

* **Vercel Account** - `Sign up at Vercel <https://vercel.com/signup>`_
* **GitHub Repository** - Your RepoMind AI code
* **API Keys** - DeepSeek AI and other required services

Quick Deployment
----------------

**Method 1: One-Click Deploy**

Deploy directly from GitHub:

.. image:: https://vercel.com/button
   :target: https://vercel.com/new/clone?repository-url=https://github.com/itrimble/repomind-ai
   :alt: Deploy with Vercel

**Method 2: Vercel CLI**

.. code-block:: bash

   # Install Vercel CLI
   npm i -g vercel

   # Login to Vercel
   vercel login

   # Deploy from project directory
   cd repomind-ai
   vercel

**Method 3: GitHub Integration**

1. Import project from GitHub in Vercel dashboard
2. Configure environment variables
3. Deploy automatically on push

Configuration
-------------

**Vercel Configuration File**

The project includes :code:`vercel.json` with optimized settings:

.. code-block:: json

   {
     "buildCommand": "pnpm run build",
     "outputDirectory": ".next",
     "devCommand": "pnpm run dev",
     "installCommand": "pnpm install",
     "framework": "nextjs"
   }

Environment Variables
--------------------

**Required Variables**
~~~~~~~~~~~~~~~~~~~~~

Set these in Vercel Dashboard → Project → Settings → Environment Variables:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Variable
     - Value
   * - :code:`DEEPSEEK_API_KEY`
     - Your DeepSeek AI API key
   * - :code:`DATABASE_URL`
     - PostgreSQL connection string
   * - :code:`NEXTAUTH_SECRET`
     - Random string for NextAuth.js
   * - :code:`NEXTAUTH_URL`
     - Your Vercel deployment URL

**Optional Variables**
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Variable
     - Value
   * - :code:`GITHUB_TOKEN`
     - GitHub personal access token
   * - :code:`POSTHOG_KEY`
     - PostHog analytics key
   * - :code:`POSTHOG_HOST`
     - PostHog host URL

**Setting Environment Variables**

.. code-block:: bash

   # Using Vercel CLI
   vercel env add DEEPSEEK_API_KEY
   vercel env add DATABASE_URL
   vercel env add NEXTAUTH_SECRET

Database Setup
--------------

**Option 1: Vercel Postgres**

.. code-block:: bash

   # Add Vercel Postgres
   vercel postgres create

   # Connect to project
   vercel env pull

**Option 2: External PostgreSQL**

Use services like:

* **Supabase** - `https://supabase.com <https://supabase.com>`_
* **PlanetScale** - `https://planetscale.com <https://planetscale.com>`_
* **Railway** - `https://railway.app <https://railway.app>`_

Custom Domain
-------------

**Add Custom Domain**

1. Go to Vercel Dashboard → Project → Settings → Domains
2. Add your domain (e.g., :code:`repomind.yourcompany.com`)
3. Configure DNS records as shown
4. SSL certificate is automatically provisioned

**DNS Configuration**

.. code-block:: text

   Type: CNAME
   Name: repomind (or @)
   Value: cname.vercel-dns.com

Performance Optimization
-----------------------

**Edge Functions**

The project uses Vercel Edge Runtime for optimal performance:

.. code-block:: typescript

   // src/app/api/analyze/route.ts
   export const runtime = 'edge'

**CDN Configuration**

Vercel automatically handles:

* Global CDN distribution
* Image optimization
* Static asset caching
* Brotli compression

**Caching Strategy**

.. code-block:: json

   {
     "headers": [
       {
         "source": "/api/(.*)",
         "headers": [
           {
             "key": "Cache-Control",
             "value": "s-maxage=300, stale-while-revalidate=86400"
           }
         ]
       }
     ]
   }

Monitoring
----------

**Vercel Analytics**

Enable in Vercel Dashboard → Project → Analytics:

* Core Web Vitals
* Page load times
* Geographic performance
* Real user metrics

**Error Tracking**

Configure error reporting:

.. code-block:: typescript

   // src/lib/error-tracking.ts
   export function reportError(error: Error) {
     if (process.env.NODE_ENV === 'production') {
       // Report to your error tracking service
       console.error('Production error:', error)
     }
   }

**Performance Monitoring**

.. code-block:: typescript

   // src/lib/analytics.ts
   export function trackPerformance(name: string, value: number) {
     if (typeof window !== 'undefined') {
       // Track performance metrics
       analytics.track('Performance', { name, value })
     }
   }

CI/CD Integration
----------------

**GitHub Actions**

The project includes automated deployment:

.. code-block:: yaml

   # .github/workflows/ci-cd.yml
   deploy-vercel:
     runs-on: ubuntu-latest
     steps:
       - uses: actions/checkout@v4
       - name: Deploy to Vercel
         run: vercel deploy --prod --token=${{ secrets.VERCEL_TOKEN }}

**Required Secrets**

Add to GitHub repository secrets:

* :code:`VERCEL_TOKEN` - Vercel API token
* :code:`VERCEL_ORG_ID` - Vercel organization ID
* :code:`VERCEL_PROJECT_ID` - Vercel project ID

Security Configuration
---------------------

**Security Headers**

Configured in :code:`vercel.json`:

.. code-block:: json

   {
     "headers": [
       {
         "source": "/(.*)",
         "headers": [
           { "key": "X-Frame-Options", "value": "DENY" },
           { "key": "X-Content-Type-Options", "value": "nosniff" },
           { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
         ]
       }
     ]
   }

**Environment Security**

* Never commit secrets to repository
* Use Vercel's environment variable encryption
* Rotate API keys regularly
* Enable two-factor authentication

Troubleshooting
--------------

**Common Issues**
~~~~~~~~~~~~~~~~

.. warning::
   **Build Failures**: Check build logs in Vercel dashboard
   
   .. code-block:: bash
   
      # Test build locally
      pnpm run build

.. note::
   **Environment Variable Issues**: Verify all required variables are set
   
   .. code-block:: bash
   
      # Check environment variables
      vercel env ls

**Performance Issues**
~~~~~~~~~~~~~~~~~~~~~

* Check bundle analyzer: :code:`ANALYZE=true pnpm run build`
* Review Lighthouse scores in CI/CD
* Monitor Core Web Vitals in Vercel Analytics

**Database Connection Issues**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Verify :code:`DATABASE_URL` format
* Check database connection limits
* Consider connection pooling

Scaling
-------

**Automatic Scaling**

Vercel automatically handles:

* Traffic spikes
* Geographic distribution
* Edge function scaling
* Bandwidth optimization

**Enterprise Features**

For high-traffic applications:

* **Vercel Pro/Enterprise** - Advanced analytics and support
* **Edge Config** - Global configuration management
* **KV Storage** - Distributed key-value storage
* **Blob Storage** - Large file storage

Next Steps
----------

After deployment:

1. **Monitor Performance** - Check Vercel Analytics dashboard
2. **Set Up Alerts** - Configure error and performance alerts
3. **Custom Domain** - Add your company domain
4. **Team Access** - Invite team members to Vercel project
5. **Backup Strategy** - Plan for data backup and recovery

Support
-------

* **Vercel Documentation** - `https://vercel.com/docs <https://vercel.com/docs>`_
* **Community** - `Vercel Discord <https://vercel.com/discord>`_
* **Enterprise Support** - Available with Pro/Enterprise plans