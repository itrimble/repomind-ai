🧠 RepoMind AI Documentation
================================

**AI-powered repository analysis and visualization platform**

.. image:: https://img.shields.io/badge/Next.js-15.3.3-black
   :target: https://nextjs.org/
   :alt: Next.js

.. image:: https://img.shields.io/badge/TypeScript-5.5.3-blue
   :target: https://www.typescriptlang.org/
   :alt: TypeScript

.. image:: https://img.shields.io/badge/Three.js-Interactive%20Graphics-red
   :target: https://threejs.org/
   :alt: Three.js

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/itrimble/repomind-ai/blob/main/LICENSE
   :alt: License

RepoMind AI transforms complex codebases into interactive, understandable diagrams using cutting-edge AI and 3D visualization technology. Built for developers, by developers.

🚀 **Quick Links:**

* **Repository**: `GitHub <https://github.com/itrimble/repomind-ai>`_
* **Live Demo**: `RepoMind AI <https://repomind-ai.vercel.app>`_
* **API Documentation**: `API Docs <https://repomind-ai.vercel.app/docs>`_

Features
--------

🎯 **Core Capabilities**

* **📊 Interactive Code Visualization** - Transform repositories into beautiful, navigable diagrams
* **🤖 AI-Powered Analysis** - Intelligent code insights and documentation generation  
* **🎮 3D Interactive Experience** - Three.js-powered immersive code exploration
* **⚡ Real-time Collaboration** - Multi-user diagram editing and sharing
* **🔍 Advanced Search & Filter** - Find and analyze specific code patterns
* **📱 Responsive Design** - Works seamlessly across all devices

🛠 **Technical Features**

* **🔧 Full Debugging Suite** - Comprehensive VS Code and browser debugging
* **🏗 Modular Architecture** - Clean, maintainable component structure
* **🎨 Modern UI/UX** - ShadCN UI components with Tailwind styling
* **📈 Performance Optimized** - Turbo mode and optimized rendering
* **🔒 Type-Safe** - Full TypeScript implementation
* **🌙 Dark/Light Mode** - Theme switching with next-themes

Technology Stack
----------------

**Frontend**
~~~~~~~~~~~~

* **Next.js 15.3.3** - React framework with App Router
* **TypeScript 5.5.3** - Type-safe development
* **Three.js** - 3D graphics and interactive visualizations
* **ShadCN UI** - Modern, accessible component library
* **Tailwind CSS** - Utility-first styling

**Backend**
~~~~~~~~~~~

* **Python 3.13** - Backend API services
* **FastAPI** - High-performance API framework
* **PostgreSQL** - Primary database with Drizzle ORM
* **DeepSeek AI** - AI-powered code analysis
* **Docker** - Containerized deployment

**Development Tools**
~~~~~~~~~~~~~~~~~~~~

* **VS Code/Cursor** - Enhanced debugging support
* **pnpm 9.13.0** - Fast, efficient package management
* **ESLint + Prettier** - Code quality and formatting
* **Turbo** - Accelerated development builds

Table of Contents
----------------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   getting-started/installation
   getting-started/quick-start
   getting-started/configuration

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user-guide/interface
   user-guide/repository-analysis
   user-guide/visualization
   user-guide/collaboration

.. toctree::
   :maxdepth: 2
   :caption: Development

   development/setup
   development/debugging
   development/architecture
   development/contributing

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/authentication
   api/endpoints
   api/webhooks
   api/rate-limits

.. toctree::
   :maxdepth: 2
   :caption: Deployment

   deployment/vercel
   deployment/docker
   deployment/environment-variables
   deployment/monitoring

.. toctree::
   :maxdepth: 2
   :caption: Advanced

   advanced/three-js-integration
   advanced/ai-models
   advanced/performance-optimization
   advanced/security

.. toctree::
   :maxdepth: 2
   :caption: Reference

   reference/troubleshooting
   reference/faq
   reference/changelog
   reference/license

Quick Start
----------

1. **Clone the Repository**

   .. code-block:: bash

      git clone https://github.com/itrimble/repomind-ai.git
      cd repomind-ai

2. **Install Dependencies**

   .. code-block:: bash

      pnpm install

3. **Set Up Environment**

   .. code-block:: bash

      cp .env.example .env
      # Edit .env with your configuration

4. **Start Development**

   .. code-block:: bash

      # Frontend (port 6002)
      pnpm run dev

      # Backend (port 8000)  
      docker-compose up --build -d

5. **Access Application**

   * **Frontend**: http://localhost:6002
   * **Backend API**: http://localhost:8000
   * **API Docs**: http://localhost:8000/docs

Debugging Guide
--------------

RepoMind AI includes comprehensive debugging capabilities:

**VS Code Debugging**

1. Open project: :code:`code .`
2. Press :kbd:`⇧+⌘+D` (Debug panel)
3. Select configuration:
   
   * **"Next.js: debug server-side"** - API routes & server components
   * **"Next.js: debug client-side"** - React components  
   * **"Next.js: debug full stack"** - Complete debugging

4. Press :kbd:`F5` to start debugging

**Debug Scripts**

.. code-block:: bash

   # Server-side debugging
   pnpm run dev:debug

   # Browser DevTools integration
   NODE_OPTIONS='--inspect' pnpm run dev

Screenshots
----------

.. image:: screenshots/hero-section.png
   :alt: RepoMind AI Hero Section
   :width: 800px

*Main interface showcasing AI-powered repository analysis*

.. image:: screenshots/demo-section.png  
   :alt: Interactive Demo Section
   :width: 800px

*Interactive demo with popular open-source repositories*

Community & Support
------------------

* **🐛 Issues**: `GitHub Issues <https://github.com/itrimble/repomind-ai/issues>`_
* **💬 Discussions**: `GitHub Discussions <https://github.com/itrimble/repomind-ai/discussions>`_
* **📚 Wiki**: `Project Wiki <https://github.com/itrimble/repomind-ai/wiki>`_

Contributing
-----------

We welcome contributions! Please see our :doc:`development/contributing` guide for details.

License
-------

This project is licensed under the MIT License - see the `LICENSE <https://github.com/itrimble/repomind-ai/blob/main/LICENSE>`_ file for details.

---

**Built with ❤️ by developers, for developers**

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`