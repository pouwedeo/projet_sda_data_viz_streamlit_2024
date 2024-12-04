import  streamlit as st


st.markdown("""

          <style>
           p{
              text-align: justify;          
            }
          </style>
          
          <h1> Contexte du projet</h1>
          
          <p> 
              Le financement participatif, ou crowdfunding, est devenu un levier essentiel pour soutenir des 
              projets créatifs, entrepreneuriaux et innovants dans divers domaines. Parmi les plateformes de 
              financement participatif, Kickstarter se distingue par son modèle permettant aux créateurs de 
              collecter des fonds pour leurs projets grâce à des contributeurs du monde entier. Depuis sa 
              création, Kickstarter a permis de financer des milliers de projets, mais tous n'ont pas rencontré 
              le succès escompté. Comprendre les facteurs qui influencent le succès ou l'échec d'une campagne
               Kickstarter est une question cruciale pour les porteurs de projet et les contributeurs.
             Dans ce contexte, le jeu de données Kickstarter 2020 (https://www.kaggle.com/datasets/kevinennis/kickstarter-2020) offre une opportunité unique d'explorer les
             caractéristiques des projets hébergés sur la plateforme au cours de l'année 2020. Ce jeu de données
            contient des informations détaillées sur chaque projet, telles que le nom, la catégorie, le montant
            demandé, les fonds collectés, la localisation et l’état final de la campagne (successful, failed, etc.). 
           En analysant ces données, il devient possible de dégager des tendances et des insights pour identifier les 
          facteurs déterminants du succès.

          </p>
          
          <h2>Objectifs du projet</h2>
          <p> 
            Quels sont les principaux facteurs qui influencent le succès ou l'échec d'une campagne Kickstarter en 2020, et comment
             peut-on prédire ce succès à partir des caractéristiques d’un projet ?
             
             <ul> 
              <li> 
                <strong> Explorer et analyser les données Kickstarter 2020 </strong>
                afin de comprendre la distribution et les tendances des campagnes.
              </li>
              <li> 
                 <strong>Identifier les facteurs influençant le succès des projets </strong> 
                 en examinant des variables telles que la catégorie, la localisation, le montant demandé,
                  et la durée de la campagne.
              </li>
               <li> 
                 <strong>Proposer des modèles prédictifs </strong> 
                 capables d’estimer la probabilité de succès d’un projet en fonction de ses caractéristiques.
              </li>
               <li> 
                 Fournir des recommandations pratiques pour optimiser les campagnes de financement sur Kickstarter.
              </li>
             </ul>
           </p>
           
           <h1>Description du jeu de données </h1>
           <p>
           Données détaillées sur les projets (titres, catégories, objectifs financiers, montants levés, etc.).
           Métadonnées sur les campagnes (durée, localisation, description, statut).
           Données temporelles (dates de début, de fin, mise à jour).

           </p>
           
           <h2> Description des variables </h2>
           <div>
           
           <table>
           <tr>
           <th>Variable </th>
           <th>Description </th>
           </tr>
             <tr> 
           <td>id</td>
           <td>Identifiant unique du projet.</td>
           </tr>
             <tr> 
           <td>name	</td>
           <td> Nom du projet.</td>
           </tr>
             <tr> 
           <td>blurb</td>
           <td>	Description courte du projet. </td>
           </tr>
             <tr> 
           <td>category	</td>
           <td>Catégorie du projet (ex : Musique, Jeux, Technologie). </td>
           </tr>
           <tr> 
           <td> creator</td>
           <td>Informations sur le créateur (nom, statut de vérification).</td>
           </tr>
           
           <tr> 
           <td>goal</td>
           <td>	Objectif financier fixé en devise locale.  </td>
           </tr>
           <tr> 
           <td>pledged </td>
           <td>Montant collecté en devise locale.</td>
           </tr>
           <tr> 
           <td>backers_count</td>
           <td>	Nombre de financeurs ayant soutenu le projet.  </td>
           </tr>
           <tr> 
           <td>usd_pledged</td>
           <td>	Montant collecté converti en dollars USD.  </td>
           </tr>
           <tr> 
           <td>currency </td>
           <td> Devise utilisée dans la campagne.</td>
           </tr>
           <tr> 
           <td>state </td>
           <td>	Statut de la campagne (ex : succeeded, failed, canceled). </td>
           </tr>
           <tr> 
           <td>spotlight</td>
           <td>	Si le projet a été mis en avant par Kickstarter.  </td>
           </tr>
           <tr> 
           <td>staff_pick</td>
           <td>	Si le projet a été sélectionné par l'équipe Kickstarter.Données Géographiques </td>
           </tr>
           <tr> 
           <td>country	 </td>
           <td> Pays d'origine du projet.</td>
           </tr>
           <tr> 
           <td>location</td>
           <td> Ville où le projet est basé.Temporalité</td>
           </tr>
            <tr> 
           <td>launched_at	</td>
           <td> Date et heure de lancement de la campagne.</td>
           </tr>
            <tr> 
           <td>deadline	</td>
           <td>Date limite de la campagne. </td>
           </tr>
            <tr> 
           <td>duration	</td>
           <td>Durée totale de la campagne en jours. Utilisations Courantes </td>
           </tr>
          
           </table>
           </div>
            """, unsafe_allow_html=True)