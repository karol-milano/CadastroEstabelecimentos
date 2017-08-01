--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.7
-- Dumped by pg_dump version 9.5.7

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: trabalhoES
--

CREATE TABLE alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE alembic_version OWNER TO "trabalhoES";

--
-- Name: comments; Type: TABLE; Schema: public; Owner: trabalhoES
--

CREATE TABLE comments (
    id integer NOT NULL,
    text character varying,
    user_id integer,
    enterprise_id integer
);


ALTER TABLE comments OWNER TO "trabalhoES";

--
-- Name: comments_id_seq; Type: SEQUENCE; Schema: public; Owner: trabalhoES
--

CREATE SEQUENCE comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE comments_id_seq OWNER TO "trabalhoES";

--
-- Name: comments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trabalhoES
--

ALTER SEQUENCE comments_id_seq OWNED BY comments.id;


--
-- Name: enterprise_items; Type: TABLE; Schema: public; Owner: trabalhoES
--

CREATE TABLE enterprise_items (
    id integer NOT NULL,
    item_id integer,
    enterprise_id integer
);


ALTER TABLE enterprise_items OWNER TO "trabalhoES";

--
-- Name: enterprise_items_id_seq; Type: SEQUENCE; Schema: public; Owner: trabalhoES
--

CREATE SEQUENCE enterprise_items_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE enterprise_items_id_seq OWNER TO "trabalhoES";

--
-- Name: enterprise_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trabalhoES
--

ALTER SEQUENCE enterprise_items_id_seq OWNED BY enterprise_items.id;


--
-- Name: enterprise_ratings; Type: TABLE; Schema: public; Owner: trabalhoES
--

CREATE TABLE enterprise_ratings (
    id integer NOT NULL,
    grade double precision,
    user_id integer,
    enterprise_id integer
);


ALTER TABLE enterprise_ratings OWNER TO "trabalhoES";

--
-- Name: enterprise_ratings_id_seq; Type: SEQUENCE; Schema: public; Owner: trabalhoES
--

CREATE SEQUENCE enterprise_ratings_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE enterprise_ratings_id_seq OWNER TO "trabalhoES";

--
-- Name: enterprise_ratings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trabalhoES
--

ALTER SEQUENCE enterprise_ratings_id_seq OWNED BY enterprise_ratings.id;


--
-- Name: enterprises; Type: TABLE; Schema: public; Owner: trabalhoES
--

CREATE TABLE enterprises (
    id integer NOT NULL,
    name character varying,
    phone character varying,
    address character varying
);


ALTER TABLE enterprises OWNER TO "trabalhoES";

--
-- Name: enterprises_id_seq; Type: SEQUENCE; Schema: public; Owner: trabalhoES
--

CREATE SEQUENCE enterprises_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE enterprises_id_seq OWNER TO "trabalhoES";

--
-- Name: enterprises_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trabalhoES
--

ALTER SEQUENCE enterprises_id_seq OWNED BY enterprises.id;


--
-- Name: item_ratings; Type: TABLE; Schema: public; Owner: trabalhoES
--

CREATE TABLE item_ratings (
    id integer NOT NULL,
    grade double precision,
    user_id integer,
    enterprise_item_id integer
);


ALTER TABLE item_ratings OWNER TO "trabalhoES";

--
-- Name: item_ratings_id_seq; Type: SEQUENCE; Schema: public; Owner: trabalhoES
--

CREATE SEQUENCE item_ratings_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE item_ratings_id_seq OWNER TO "trabalhoES";

--
-- Name: item_ratings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trabalhoES
--

ALTER SEQUENCE item_ratings_id_seq OWNED BY item_ratings.id;


--
-- Name: items; Type: TABLE; Schema: public; Owner: trabalhoES
--

CREATE TABLE items (
    id integer NOT NULL,
    description character varying
);


ALTER TABLE items OWNER TO "trabalhoES";

--
-- Name: items_id_seq; Type: SEQUENCE; Schema: public; Owner: trabalhoES
--

CREATE SEQUENCE items_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE items_id_seq OWNER TO "trabalhoES";

--
-- Name: items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trabalhoES
--

ALTER SEQUENCE items_id_seq OWNED BY items.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: trabalhoES
--

CREATE TABLE users (
    id integer NOT NULL,
    name character varying,
    phone character varying,
    email character varying
);


ALTER TABLE users OWNER TO "trabalhoES";

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: trabalhoES
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_id_seq OWNER TO "trabalhoES";

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: trabalhoES
--

ALTER SEQUENCE users_id_seq OWNED BY users.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY comments ALTER COLUMN id SET DEFAULT nextval('comments_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprise_items ALTER COLUMN id SET DEFAULT nextval('enterprise_items_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprise_ratings ALTER COLUMN id SET DEFAULT nextval('enterprise_ratings_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprises ALTER COLUMN id SET DEFAULT nextval('enterprises_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY item_ratings ALTER COLUMN id SET DEFAULT nextval('item_ratings_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY items ALTER COLUMN id SET DEFAULT nextval('items_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY users ALTER COLUMN id SET DEFAULT nextval('users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: trabalhoES
--

INSERT INTO alembic_version (version_num) VALUES ('dea0de99a0bc');


--
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: trabalhoES
--

INSERT INTO comments (id, text, user_id, enterprise_id) VALUES (1, 'Um texto', 1, 1);
INSERT INTO comments (id, text, user_id, enterprise_id) VALUES (2, 'Outro texto', 2, 1);
INSERT INTO comments (id, text, user_id, enterprise_id) VALUES (3, 'testes', NULL, 8);
INSERT INTO comments (id, text, user_id, enterprise_id) VALUES (4, 'dsfsdfdsfs', NULL, 8);
INSERT INTO comments (id, text, user_id, enterprise_id) VALUES (5, 'zfszdf zsdfszdfszf sdzfsd ', NULL, 1);
INSERT INTO comments (id, text, user_id, enterprise_id) VALUES (6, 'fsdfdsfsdfds fdsfd', NULL, 1);
INSERT INTO comments (id, text, user_id, enterprise_id) VALUES (7, 'fsdfdsfsdfds fdsfd', NULL, 1);


--
-- Name: comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: trabalhoES
--

SELECT pg_catalog.setval('comments_id_seq', 7, true);


--
-- Data for Name: enterprise_items; Type: TABLE DATA; Schema: public; Owner: trabalhoES
--

INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (1, 1, 1);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (2, 2, 1);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (3, 3, 1);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (4, 4, 1);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (5, 1, 8);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (6, 2, 8);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (7, 3, 8);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (8, 4, 8);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (9, 5, 8);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (10, 6, 8);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (11, 7, 8);
INSERT INTO enterprise_items (id, item_id, enterprise_id) VALUES (12, 8, 8);


--
-- Name: enterprise_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: trabalhoES
--

SELECT pg_catalog.setval('enterprise_items_id_seq', 12, true);


--
-- Data for Name: enterprise_ratings; Type: TABLE DATA; Schema: public; Owner: trabalhoES
--

INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (1, 5.29999999999999982, 1, 1);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (2, 5, NULL, 1);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (3, 4, NULL, 1);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (4, 3, NULL, 8);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (5, 5, NULL, 8);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (6, 5, NULL, 8);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (7, 5, NULL, 8);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (8, 5, NULL, 8);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (9, 5, NULL, 8);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (10, 5, NULL, 8);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (11, 5, NULL, 8);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (12, 5, NULL, 8);
INSERT INTO enterprise_ratings (id, grade, user_id, enterprise_id) VALUES (13, 5, NULL, 8);


--
-- Name: enterprise_ratings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: trabalhoES
--

SELECT pg_catalog.setval('enterprise_ratings_id_seq', 13, true);


--
-- Data for Name: enterprises; Type: TABLE DATA; Schema: public; Owner: trabalhoES
--

INSERT INTO enterprises (id, name, phone, address) VALUES (1, 'Hokkar', '1234567', 'Rua teste, 67 - Um bairro');
INSERT INTO enterprises (id, name, phone, address) VALUES (2, 'Dexter', '(67) 98457-6683', 'teste');
INSERT INTO enterprises (id, name, phone, address) VALUES (3, 'Outro', '123445656', 'werwfdfsd');
INSERT INTO enterprises (id, name, phone, address) VALUES (4, '3Outro', '67999333', 'teste');
INSERT INTO enterprises (id, name, phone, address) VALUES (5, '3Outro', '67999333', 'werwfdfsd');
INSERT INTO enterprises (id, name, phone, address) VALUES (6, 'Dexter2', '67999333', 'werwfdfsd');
INSERT INTO enterprises (id, name, phone, address) VALUES (7, '3Outro342', '23424324', 'werewweewffaefaew');
INSERT INTO enterprises (id, name, phone, address) VALUES (8, '3Outrodas', '67999333', 'teste');


--
-- Name: enterprises_id_seq; Type: SEQUENCE SET; Schema: public; Owner: trabalhoES
--

SELECT pg_catalog.setval('enterprises_id_seq', 8, true);


--
-- Data for Name: item_ratings; Type: TABLE DATA; Schema: public; Owner: trabalhoES
--



--
-- Name: item_ratings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: trabalhoES
--

SELECT pg_catalog.setval('item_ratings_id_seq', 1, false);


--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: trabalhoES
--

INSERT INTO items (id, description) VALUES (1, 'Banheiro familiar');
INSERT INTO items (id, description) VALUES (2, 'Fraldário');
INSERT INTO items (id, description) VALUES (3, 'Espaço kids');
INSERT INTO items (id, description) VALUES (4, 'Monitor infantil');
INSERT INTO items (id, description) VALUES (5, 'Microondas');
INSERT INTO items (id, description) VALUES (6, 'Acessibilidade');
INSERT INTO items (id, description) VALUES (7, 'Estacionamento coberto');
INSERT INTO items (id, description) VALUES (8, 'Elevador');


--
-- Name: items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: trabalhoES
--

SELECT pg_catalog.setval('items_id_seq', 8, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: trabalhoES
--

INSERT INTO users (id, name, phone, email) VALUES (1, 'Karolina Martins', '(67) 99202-5883', 'karol.milano@gmail.com');
INSERT INTO users (id, name, phone, email) VALUES (2, 'Pedro Henrique', '(67) 98457-6683', 'pedro.silva@ifms.edu.br');


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: trabalhoES
--

SELECT pg_catalog.setval('users_id_seq', 2, true);


--
-- Name: alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: comments_pkey; Type: CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (id);


--
-- Name: enterprise_items_pkey; Type: CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprise_items
    ADD CONSTRAINT enterprise_items_pkey PRIMARY KEY (id);


--
-- Name: enterprise_ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprise_ratings
    ADD CONSTRAINT enterprise_ratings_pkey PRIMARY KEY (id);


--
-- Name: enterprises_pkey; Type: CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprises
    ADD CONSTRAINT enterprises_pkey PRIMARY KEY (id);


--
-- Name: item_ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY item_ratings
    ADD CONSTRAINT item_ratings_pkey PRIMARY KEY (id);


--
-- Name: items_pkey; Type: CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY items
    ADD CONSTRAINT items_pkey PRIMARY KEY (id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: comments_enterprise_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY comments
    ADD CONSTRAINT comments_enterprise_id_fkey FOREIGN KEY (enterprise_id) REFERENCES enterprises(id);


--
-- Name: comments_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY comments
    ADD CONSTRAINT comments_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id);


--
-- Name: enterprise_items_enterprise_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprise_items
    ADD CONSTRAINT enterprise_items_enterprise_id_fkey FOREIGN KEY (enterprise_id) REFERENCES enterprises(id);


--
-- Name: enterprise_items_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprise_items
    ADD CONSTRAINT enterprise_items_item_id_fkey FOREIGN KEY (item_id) REFERENCES items(id);


--
-- Name: enterprise_ratings_enterprise_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprise_ratings
    ADD CONSTRAINT enterprise_ratings_enterprise_id_fkey FOREIGN KEY (enterprise_id) REFERENCES enterprises(id);


--
-- Name: enterprise_ratings_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY enterprise_ratings
    ADD CONSTRAINT enterprise_ratings_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id);


--
-- Name: item_ratings_enterprise_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY item_ratings
    ADD CONSTRAINT item_ratings_enterprise_item_id_fkey FOREIGN KEY (enterprise_item_id) REFERENCES enterprise_items(id);


--
-- Name: item_ratings_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: trabalhoES
--

ALTER TABLE ONLY item_ratings
    ADD CONSTRAINT item_ratings_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

