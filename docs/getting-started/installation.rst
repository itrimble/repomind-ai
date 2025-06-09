Installation Guide
==================

This guide will help you set up RepoMind AI for development and production use.

Prerequisites
------------

Before installing RepoMind AI, ensure you have the following:

**Required**
~~~~~~~~~~~~

* **Node.js 18.17+** - `Download Node.js <https://nodejs.org/>`_
* **pnpm 9.13.0+** - Install with: :code:`npm install -g pnpm`
* **Python 3.13+** - `Download Python <https://www.python.org/downloads/>`_
* **PostgreSQL 14+** - Database (can use Docker)
* **Docker** - For backend services (optional but recommended)

**Optional**
~~~~~~~~~~~~

* **VS Code** - For enhanced debugging experience
* **Git** - Version control

System Requirements
------------------

**Minimum**
~~~~~~~~~~~

* **RAM**: 8GB
* **Storage**: 2GB free space
* **OS**: macOS 12+, Windows 10+, or Ubuntu 20.04+

**Recommended**
~~~~~~~~~~~~~~~

* **RAM**: 16GB+
* **Storage**: 5GB+ free space
* **CPU**: Multi-core processor for optimal performance

Installation Methods
-------------------

Method 1: Development Setup (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Clone Repository**

   .. code-block:: bash

      git clone https://github.com/itrimble/repomind-ai.git
      cd repomind-ai

2. **Install Dependencies**

   .. code-block:: bash

      # Install frontend dependencies
      pnpm install

3. **Environment Configuration**

   .. code-block:: bash

      cp .env.example .env

   Edit the :code:`.env` file with your configuration:

   .. code-block:: env

      # Required for AI analysis
      DEEPSEEK_API_KEY="your_deepseek_api_key"
      
      # Required for private repos
      GITHUB_TOKEN="your_github_personal_access_token"
      
      # Database (auto-configured by start-database.sh)
      DATABASE_URL="postgresql://postgres:password@localhost:5432/repomind"
      
      # Optional: Analytics
      POSTHOG_KEY="your_posthog_key"

4. **Database Setup**

   .. code-block:: bash

      # Automated setup (recommended)
      chmod +x start-database.sh
      ./start-database.sh

      # Apply schema
      pnpm run db:push

5. **Start Services**

   .. code-block:: bash

      # Terminal 1: Frontend
      pnpm run dev

      # Terminal 2: Backend
      docker-compose up --build -d

6. **Verify Installation**

   Open your browser and navigate to:

   * **Frontend**: http://localhost:6002
   * **Backend API**: http://localhost:8000
   * **API Documentation**: http://localhost:8000/docs

Method 2: Docker Setup
~~~~~~~~~~~~~~~~~~~~~

1. **Clone and Configure**

   .. code-block:: bash

      git clone https://github.com/itrimble/repomind-ai.git
      cd repomind-ai
      cp .env.example .env
      # Edit .env with your configuration

2. **Start with Docker Compose**

   .. code-block:: bash

      # Start all services
      docker-compose up --build

3. **Access Application**

   * **Frontend**: http://localhost:6002
   * **Backend**: http://localhost:8000

Method 3: Production Deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our :doc:`../deployment/vercel` guide for production deployment instructions.

Debugging Setup
---------------

RepoMind AI includes comprehensive debugging capabilities:

**VS Code Configuration**

The project includes pre-configured debugging settings in :code:`.vscode/launch.json`:

* **Server-side debugging** - Debug API routes and server components
* **Client-side debugging** - Debug React components in Chrome/Firefox
* **Full-stack debugging** - Combined server + client debugging

**Enable Debugging**

.. code-block:: bash

   # Start with debugging enabled
   pnpm run dev:debug

   # Or use VS Code debugger
   code .
   # Press ⇧+⌘+D, select configuration, press F5

Environment Variables
--------------------

**Required Variables**
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Variable
     - Description
   * - :code:`DEEPSEEK_API_KEY`
     - DeepSeek AI API key for code analysis
   * - :code:`DATABASE_URL`
     - PostgreSQL database connection string

**Optional Variables**
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Variable
     - Description
   * - :code:`GITHUB_TOKEN`
     - GitHub personal access token for private repos
   * - :code:`POSTHOG_KEY`
     - PostHog analytics key
   * - :code:`NEXTAUTH_SECRET`
     - NextAuth.js secret for authentication
   * - :code:`NODE_ENV`
     - Environment mode (development/production)

API Keys Setup
-------------

**DeepSeek AI API Key**
~~~~~~~~~~~~~~~~~~~~~~

1. Visit `DeepSeek Platform <https://platform.deepseek.com/>`_
2. Create an account and navigate to API Keys
3. Generate a new API key
4. Add to your :code:`.env` file: :code:`DEEPSEEK_API_KEY="your_key"`

**GitHub Token (Optional)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For private repository access:

1. Go to `GitHub Settings → Developer settings → Personal access tokens <https://github.com/settings/tokens>`_
2. Generate a new token with :code:`repo` scope
3. Add to your :code:`.env` file: :code:`GITHUB_TOKEN="your_token"`

Verification
-----------

**Frontend Health Check**
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   curl http://localhost:6002

**Backend Health Check**
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   curl http://localhost:8000/health

**Database Connection**
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pnpm run db:studio

Troubleshooting
--------------

**Common Issues**
~~~~~~~~~~~~~~~~

.. note::
   **Port Conflicts**: If ports 6002 or 8000 are in use:
   
   .. code-block:: bash
   
      # Kill processes using the ports
      lsof -ti:6002 | xargs kill -9
      lsof -ti:8000 | xargs kill -9

.. warning::
   **Database Connection Errors**: Ensure PostgreSQL is running:
   
   .. code-block:: bash
   
      # Restart database
      ./start-database.sh

**Build Errors**
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Clear cache and reinstall
   rm -rf .next node_modules
   pnpm install
   pnpm run build

**Environment Issues**
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Verify environment variables
   node -e "console.log(process.env.DEEPSEEK_API_KEY ? 'API key loaded' : 'API key missing')"

Next Steps
----------

After successful installation:

1. :doc:`quick-start` - Learn basic usage
2. :doc:`configuration` - Advanced configuration options
3. :doc:`../development/debugging` - Set up debugging environment
4. :doc:`../user-guide/interface` - Explore the user interface

Need Help?
----------

* **Documentation**: Continue reading this guide
* **Issues**: `GitHub Issues <https://github.com/itrimble/repomind-ai/issues>`_
* **Discussions**: `GitHub Discussions <https://github.com/itrimble/repomind-ai/discussions>`_